<script>
  // import "./timeline.css";
  let player1;
  let player1State;
  import Youtube from "../lib/Youtube.svelte";
  import { currentTimeLine } from "../store/store";

  let currentTime = 0;

  currentTimeLine.subscribe((value) => {
    currentTime = value;
  });
</script>

<!-- <p>Join</p> -->

<hr />

<Youtube
  videoId="M7lc1UVf-VE"
  on:PlayerStateChangeString={({ detail }) => (player1State = detail)}
  bind:this={player1}
/><br />
<button on:click={() => player1.play()}> play v1 </button>
<!-- <button on:click={() => player1.seekTo(582.736988, true)}> Seekto </button> -->
<input type="range" value={currentTime} on:change />

<!-- Player 1 State: {player1State} -->
<style>
  input[type="range"] {
    /* padding: 0 10px; */
    width: 80%;
  }
</style>
