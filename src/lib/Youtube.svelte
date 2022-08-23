<script>
  // @ts-nocheck
  let iframeApiReady = false;

  import { setContext, onMount } from "svelte";
  var tag = document.createElement("script");
  tag.src = "https://www.youtube.com/iframe_api";
  var firstScriptTag = document.getElementsByTagName("script")[0];
  firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

  // @ts-ignore
  onMount(async () => {
    window.onYouTubeIframeAPIReady = () =>
      window.dispatchEvent(new Event("iframeApiReady"));
  });

  import { createEventDispatcher } from "svelte";
  import { getContext } from "svelte";
  import { currentTimeLine } from "../store/store";

  export let videoId;

  let player;
  let divId = "player_" + parseInt(Math.random() * 109999);
  export function play() {
    player.playVideo();
  }
  export function pause() {
    player.pauseVideo();
  }
  export function seekTo(time, allowSeekAhead) {
    let newTime = time * player.getDuration();
    player.seekTo(newTime, allowSeekAhead);
  }
  function updateTime() {
    // return (player.getCurrentTime / player.getDuration) * 100;
    let currentTime = (player.getCurrentTime() / player.getDuration()) * 100;
    currentTimeLine.update((n) => (n = currentTime));
  }

  const dispatch = createEventDispatcher();
  window.addEventListener("iframeApiReady", function (e) {
    // console.log("yo", divId);
    player = new YT.Player(divId, {
      height: "390",
      width: "640",
      videoId,
      events: {
        onReady: playerIsReady,
        onStateChange: playerStateChange,
      },
    });
  });
  function playerStateChange({ data }) {
    dispatch("PlayerStateChange", data);
    // console.log(data);
    let strReturn = "";
    if (data == -1) {
      strReturn = "(unstarted)";
    }
    if (data == 0) {
      strReturn = "(ended)";
    }
    if (data == 1) {
      strReturn = "(playing)";
    }
    if (data == 2) {
      strReturn = "(paused)";
    }
    if (data == 3) {
      strReturn = "(buffering)";
    }
    if (data == 5) {
      strReturn = "(video cued).";
    }
    dispatch("PlayerStateChangeString", strReturn);
  }
  function playerIsReady() {
    updateTime();
    dispatch("Ready");
    setInterval(() => {
      dispatch("currentPlayTime", player.getCurrentTime());
      updateTime();
    }, 1000);
  }
</script>

<div id={divId} />
