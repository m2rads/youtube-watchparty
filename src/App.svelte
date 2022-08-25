<script>
  import Home from "./components/Home.svelte";
  import JoinParty from "./components/JoinParty.svelte";
  import NewParty from "./components/NewParty.svelte";

  import { isJoinRoom, isNewRoom } from "./store/store";
  let joinRoom, newRoom;
  isJoinRoom.subscribe((value) => {
    joinRoom = value;
  });

  isNewRoom.subscribe((value) => {
    newRoom = value;
  });
</script>

{#if joinRoom}
  <JoinParty />
{:else if newRoom}
  <NewParty />
{:else}
  <Home />
{/if}

<!-- <JoinParty /> -->
