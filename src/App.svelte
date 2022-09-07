<script>
  import Home from "./components/Home.svelte";
  import JoinParty from "./components/JoinParty.svelte";
  import PartyRoom from "./components/PartyRoom.svelte";

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
  <PartyRoom />
{:else if newRoom}
  <PartyRoom />
{:else}
  <Home />
{/if}

<!-- <JoinParty /> -->
