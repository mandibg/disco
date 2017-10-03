# Welcome to Sonic Pi v3.0.1
live_loop :listen do
  set_sched_ahead_time! 0.1
end
play 60
time = 1
live_loop :listen do
  message = sync "/osc/play_this"
  note = message[0]
  time = message[1]
  synth = message[2]
  #puts note
  use_synth synth
  play note
  sleep time
end



