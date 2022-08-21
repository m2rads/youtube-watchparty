<script>
  let player1, player2;
  let player1State, player2State;
  import Youtube from "../lib/Youtube.svelte";
</script>

<p>Join</p>

<!-- <hr /> -->
<!-- <Youtube
    videoId="M7lc1UVf-VE"
    on:PlayerStateChangeString={({ detail }) => (player1State = detail)}
    bind:this={player1}
  /><br />
  <button on:click={() => player1.play()}> play v1 </button><br />
  Player 1 State: {player1State} -->
