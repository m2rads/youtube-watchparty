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

  socket.on("Id", (data) => {
    roomId = data.roomId;
    username = data.username;
  });

  socket.on("on_youtube_change", (data) => {
    let timeline = data.timeline;
    console.log("player", timeline);
    player1.seekTo(timeline / 100, true);
  });

  currentTimeLine.subscribe((value) => {
    currentTime = value;
  });

  const timelineChange = (e, player) => {
    socket.emit("on_youtube_change", {
      timeline: e.target.value,
      roomId: roomId,
    });
    player1.seekTo(e.target.value / 100, true);
    // playStatus = true ? (playerStatus = false) : (playStatus = true);
  };
</script>

<p>Welcome {username}! Your room id is {roomId}</p>

<hr />

<Youtube
  videoId="M7lc1UVf-VE"
  on:PlayerStateChangeString={({ detail }) => (player1State = detail)}
  bind:this={player1}
/><br />
<div class="video-controller">
  <button
    on:click={() => {
      player1.pause();
      playStatus = true;
    }}
    class="button pause">⏮</button
  >
  {#if playStatus}
    <button
      on:click={() => {
        player1.play();
        playStatus = false;
      }}
      class="button play"
    >
      ▶️</button
    >
  {:else}
    <button
      on:click={() => {
        player1.pause();
        playStatus = true;
      }}
      class="button pause">⏸</button
    >
  {/if}
  <button
    on:click={() => {
      player1.pause();
      playStatus = true;
    }}
    class="button pause">⏭</button
  >
  <input
    type="range"
    value={currentTime}
    on:change={(e) => timelineChange(e)}
  />
</div>

<!-- Player 1 State: {player1State} -->
<style>
  input[type="range"] {
    /* padding: 0 10px; */
    width: 80%;
  }
</style>
