<script>
  // @ts-nocheck
  import { socket } from "../store/socketio";
  import Youtube from "../lib/Youtube.svelte";
  import { currentTimeLine } from "../store/store";

  let roomId;
  let username;

  let player1;
  let player1State;
  let playStatus = true;
  let currentTime = 0;
  let vid_Id = "BSGGAzsgFvk";
  let vid_url;

  socket.on("Id", (data) => {
    roomId = data.roomId;
    username = data.username;
  });

  socket.on("youtube_change", (data) => {
    let timeline = data.timeline;
    player1.seekTo(timeline / 100, true);
  });

  socket.on("player_state", (data) => {
    if (data.playState == "pause") {
      player1.pause();
      playStatus = true;
    } else if (data.playState == "play") {
      player1.play();
      playStatus = false;
    }
  });

  currentTimeLine.subscribe((value) => {
    currentTime = value;
  });

  const playerControlChange = (playerStatus) => {
    if (playerStatus == "pause") {
      player1.pause();
      playStatus = true;
      socket.emit("on_player_state", {
        playState: "pause",
        roomId: roomId,
      });
    } else {
      player1.play();
      playStatus = false;
      socket.emit("on_player_state", {
        playState: "play",
        roomId: roomId,
      });
    }
  };

  const timelineChange = (e, player) => {
    socket.emit("on_youtube_change", {
      timeline: e.target.value,
      roomId: roomId,
    });
    player1.seekTo(e.target.value / 100, true);
    playStatus = true
      ? playerControlChange("play")
      : playerControlChange("pause");
  };

  const onSeachVid = (e) => {
    e.preventDefault();
    vid_Id = vid_url.match("=([A-Za-z_+1-9]*)");
    vid_Id = vid_Id[0].substring(1);
    console.log(vid_Id);
  };
</script>

<p>Welcome {username}! Your room id is {roomId}</p>
<br />

<form on:submit={onSeachVid} class="join-form">
  <input
    v-model="vid_url"
    bind:value={vid_url}
    class="vid_url"
    placeholder="Video url..."
  />
  <button>search</button>
</form>

<hr />
{#key vid_Id}
  <Youtube
    videoId={vid_Id}
    on:PlayerStateChangeString={({ detail }) => (player1State = detail)}
    bind:this={player1}
  />
{/key}
<br />
<div class="video-controller">
  <button
    on:click={() => {
      player1.seekTo((currentTime - 5) / 100, true);
      socket.emit("on_youtube_change", {
        timeline: currentTime - 5,
        roomId: roomId,
      });
    }}
    class="button pause">⏮</button
  >
  {#if playStatus}
    <button
      on:click={() => {
        playerControlChange("play");
      }}
      class="button play"
    >
      ▶️</button
    >
  {:else}
    <button
      on:click={() => {
        playerControlChange("pause");
      }}
      class="button pause">⏸</button
    >
  {/if}
  <button
    on:click={() => {
      player1.seekTo((currentTime + 5) / 100, true);
      socket.emit("on_youtube_change", {
        timeline: currentTime + 5,
        roomId: roomId,
      });
    }}
    class="button pause">⏭</button
  >
  <input
    type="range"
    value={currentTime}
    on:change={(e) => timelineChange(e)}
  />
</div>

Player 1 State: {currentTime}

<style>
  input[type="range"] {
    /* padding: 0 10px; */
    width: 80%;
  }
</style>
