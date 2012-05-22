from header_sounds import *

#####Floris Notes#####
# The sounds used in this mod come from four different places, namely:
# - Cries of War Soundpack v3.0
# - Native Warband 1.134
# - Official Vocals Soundpack mod version v7.0
# - Sounds of Suffer v0.8
# Many thanks to xenoargh for pointing out that the .ogg format gives some unintended problems.
######################

sounds = [
#General sounds
 ("click",								sf_2d|sf_vol_1,												["min_click.wav"]),
 ("tutorial_1",							sf_2d|sf_vol_7,												["min_tutorial_1.wav"]),
 ("tutorial_2",							sf_2d|sf_vol_7,												["min_tutorial_2.wav"]),
 ("gong",								sf_2d|sf_priority_9|sf_vol_9,								["min_gong.wav"]),
 ("quest_taken",						sf_2d|sf_priority_9|sf_vol_10,								["min_quest_taken.wav"]),
 ("quest_completed",					sf_2d|sf_priority_9|sf_vol_7,								["min_quest_completed.wav"]),
 ("quest_succeeded",					sf_2d|sf_priority_9|sf_vol_7,								["min_quest_succeeded.wav"]),
 ("quest_concluded",					sf_2d|sf_priority_9|sf_vol_7,								["min_quest_concluded.wav"]),
 ("quest_failed",						sf_2d|sf_priority_9|sf_vol_7,								["min_quest_failed.wav"]),
 ("quest_cancelled",					sf_2d|sf_priority_9|sf_vol_7,								["min_quest_cancelled_01.wav","ext_quest_cancelled_02.wav"]),
# ("quest_cancelled",					sf_2d|sf_priority_9|sf_vol_7,								["min_quest_cancelled_01.wav"]),
 ("rain",								sf_2d|sf_priority_10|sf_vol_4|sf_looping,					["min_rain.wav"]),
 ("money_received",						sf_2d|sf_priority_10|sf_vol_6,								["min_money_received.wav"]),
 ("money_paid",							sf_2d|sf_priority_10|sf_vol_10,								["min_money_paid.wav"]),

#Sword clashes and swinging
 ("sword_clash_1",						0,															["min_sword_clank_metal_01.wav","min_sword_clank_metal_02.wav","min_sword_clank_metal_03.wav","min_sword_clank_metal_04.wav","min_sword_clank_metal_05.wav","min_sword_clank_metal_06.wav","min_sword_clank_metal_07.wav","min_sword_clank_metal_08.wav"]),
 ("sword_clash_2",						0,															["min_sword_clank_metal_05.wav"]),
 ("sword_clash_3",						0,															["min_sword_clank_metal_07.wav"]),
 ("sword_swing",						sf_vol_8|sf_priority_2,										["min_sword_swing_01.wav","ext_sword_swing_02.wav","ext_sword_swing_03.wav","ext_sword_swing_04.wav","ext_sword_swing_05.wav","ext_sword_swing_06.wav","ext_sword_swing_07.wav","ext_sword_swing_08.wav","ext_sword_swing_09.wav","ext_sword_swing_10.wav","ext_sword_swing_11.wav","ext_sword_swing_12.wav","ext_sword_swing_13.wav"]),
# ("sword_swing",						sf_vol_8|sf_priority_2,										["min_sword_swing_01.wav"]),

#Footsteps
 ("footstep_grass",						sf_vol_4|sf_priority_1,										["min_footstep_grass_light_01.wav","min_footstep_grass_light_02.wav","min_footstep_grass_light_03.wav","min_footstep_grass_light_04.wav","ext_footstep_grass_light_05.wav","ext_footstep_grass_light_06.wav","ext_footstep_grass_light_07.wav","ext_footstep_grass_light_08.wav","ext_footstep_grass_light_09.wav","ext_footstep_grass_light_10.wav","ext_footstep_grass_light_11.wav","ext_footstep_grass_light_12.wav","ext_footstep_grass_light_13.wav","ext_footstep_grass_light_14.wav","ext_footstep_grass_light_15.wav"]),
# ("footstep_grass",					sf_vol_4|sf_priority_1,										["min_footstep_grass_light_01.wav","min_footstep_grass_light_02.wav","min_footstep_grass_light_03.wav","min_footstep_grass_light_04.wav"]),
 ("footstep_wood",						sf_vol_6|sf_priority_1,										["min_footstep_wood_light_01.wav","min_footstep_wood_light_02.wav","min_footstep_wood_light_03.wav","min_footstep_wood_light_04.wav","ext_footstep_wood_light_05.wav","ext_footstep_wood_light_06.wav","ext_footstep_wood_light_07.wav","ext_footstep_wood_light_08.wav","ext_footstep_wood_light_09.wav","ext_footstep_wood_light_10.wav"]),
# ("footstep_wood",						sf_vol_6|sf_priority_1,										["min_footstep_wood_light_01.wav","min_footstep_wood_light_02.wav","min_footstep_wood_light_03.wav","min_footstep_wood_light_04.wav"]),
 ("footstep_water",						sf_vol_7|sf_priority_3,										["min_footstep_water_01.wav","min_footstep_water_02.wav","min_footstep_water_03.wav","min_footstep_water_04.wav","ext_footstep_water_05.wav","ext_footstep_water_06.wav","ext_footstep_water_07.wav","ext_footstep_water_08.wav","ext_footstep_water_09.wav","ext_footstep_water_10.wav","ext_footstep_water_11.wav","ext_footstep_water_12.wav","ext_footstep_water_13.wav"]),
# ("footstep_water",					sf_vol_7|sf_priority_3,										["min_footstep_water_01.wav","min_footstep_water_02.wav","min_footstep_water_03.wav","min_footstep_water_04.wav"]),
 ("footstep_horse",						sf_priority_3|sf_vol_15,									["min_footstep_horse_03b.wav","min_footstep_horse_03f.wav","min_footstep_horse_04b.wav","min_footstep_horse_04f.wav"]),
 ("footstep_horse_1b",					sf_priority_3|sf_vol_15,									["min_footstep_horse_03b.wav","min_footstep_horse_03f.wav","min_footstep_horse_04b.wav","min_footstep_horse_04f.wav"]),
 ("footstep_horse_1f",					sf_priority_3|sf_vol_15,									["min_footstep_horse_01b.wav","min_footstep_horse_01f.wav","min_footstep_horse_02b.wav","min_footstep_horse_02f.wav"]),
 ("footstep_horse_2b",					sf_priority_3|sf_vol_15,									["min_footstep_horse_01b.wav"]),
 ("footstep_horse_2f",					sf_priority_3|sf_vol_15,									["min_footstep_horse_01f.wav"]),
 ("footstep_horse_3b",					sf_priority_3|sf_vol_15,									["min_footstep_horse_02b.wav"]),
 ("footstep_horse_3f",					sf_priority_3|sf_vol_15,									["min_footstep_horse_02f.wav"]),
 ("footstep_horse_4b",					sf_priority_3|sf_vol_15,									["min_footstep_horse_03b.wav"]),
 ("footstep_horse_4f",					sf_priority_3|sf_vol_15,									["min_footstep_horse_03f.wav"]),
 ("footstep_horse_5b",					sf_priority_3|sf_vol_15,									["min_footstep_horse_04b.wav"]),
 ("footstep_horse_5f",					sf_priority_3|sf_vol_15,									["min_footstep_horse_04f.wav"]),

#Jumping
 ("jump_begin",							sf_vol_7|sf_priority_9,										["min_jump_light_b_01.wav","ext_jump_light_b_02.wav","ext_jump_light_b_03.wav","ext_jump_light_b_04.wav"]),
# ("jump_begin",						sf_vol_7|sf_priority_9,										["min_jump_light_b_01.wav"]),
 ("jump_end",							sf_vol_5|sf_priority_9,										["min_jump_light_e_01.wav","ext_jump_light_e_02.wav","ext_jump_light_e_03.wav"]),
# ("jump_end",							sf_vol_5|sf_priority_9,										["min_jump_light_e_01.wav"]),
 ("jump_begin_water",					sf_vol_9|sf_priority_9,										["min_jump_water_b_01.wav","ext_jump_water_b_02.wav","ext_jump_water_b_03.wav","ext_jump_water_b_04.wav"]),
# ("jump_begin_water",					sf_vol_9|sf_priority_9,										["min_jump_water_b_01.wav"]),
 ("jump_end_water",						sf_vol_8|sf_priority_9,										["min_jump_water_e_01.wav","ext_jump_water_e_02.wav","ext_jump_water_e_03.wav","ext_jump_water_e_04.wav","ext_jump_water_e_05.wav","ext_jump_water_e_06.wav"]),
# ("jump_end_water",					sf_vol_8|sf_priority_9,										["min_jump_water_e_01.wav"]),
 ("horse_jump_begin",					sf_vol_10|sf_priority_9,									["min_horse_jump_b_01.wav","ext_horse_jump_b_02.wav","ext_horse_jump_b_03.wav","ext_horse_jump_b_04.wav","ext_horse_jump_b_05.wav","ext_horse_jump_b_06.wav","ext_horse_jump_b_07.wav","ext_horse_jump_b_08.wav"]),
# ("horse_jump_begin",					sf_vol_10|sf_priority_9,									["min_horse_jump_b_01.wav"]),
 ("horse_jump_end",						sf_vol_10|sf_priority_9,									["min_horse_jump_e_01.wav","ext_horse_jump_e_02.wav","ext_horse_jump_e_03.wav"]),
# ("horse_jump_end",					sf_vol_10|sf_priority_9,									["min_horse_jump_e_01.wav"]),
 ("horse_jump_begin_water",				sf_vol_10|sf_priority_9,									["min_horse_jump_water_b_01.wav","ext_horse_jump_water_b_02.wav","ext_horse_jump_water_b_03.wav"]),
# ("horse_jump_begin_water",			sf_vol_10|sf_priority_9,									["min_horse_jump_water_b_01.wav"]),
 ("horse_jump_end_water",				sf_vol_10|sf_priority_9,									["min_horse_jump_water_e_01.wav","ext_horse_jump_water_e_02.wav","ext_horse_jump_water_e_03.wav","ext_horse_jump_water_e_04.wav","ext_horse_jump_water_e_05.wav","ext_horse_jump_water_e_06.wav","ext_horse_jump_water_e_07.wav","ext_horse_jump_water_e_08.wav"]),
# ("horse_jump_end_water",				sf_vol_10|sf_priority_9,									["min_horse_jump_water_e_01.wav"]),

#Ranged Weapons
 ("release_bow",						sf_vol_8,													["min_bow_shoot_01.wav","ext_bow_shoot_02.wav","ext_bow_shoot_03.wav","ext_bow_shoot_04.wav","ext_bow_shoot_05.wav","ext_bow_shoot_06.wav","ext_bow_shoot_07.wav","ext_bow_shoot_08.wav","ext_bow_shoot_09.wav","ext_bow_shoot_10.wav","ext_bow_shoot_11.wav","ext_bow_shoot_12.wav"]),
# ("release_bow",						sf_vol_8,													["min_bow_shoot_01.wav"]),
 ("release_crossbow",					sf_vol_7,													["min_crossbow_shoot_01.wav","ext_crossbow_shoot_02.wav","ext_crossbow_shoot_03.wav","ext_crossbow_shoot_04.wav","ext_crossbow_shoot_05.wav","ext_crossbow_shoot_06.wav","ext_crossbow_shoot_07.wav","ext_crossbow_shoot_08.wav"]),
# ("release_crossbow",					sf_vol_7,													["min_crossbow_shoot_01.wav"]),
 ("throw_javelin",						sf_vol_5,													["min_throw_javelin_01.wav","ext_throw_javelin_02.wav","ext_throw_javelin_03.wav","ext_throw_javelin_04.wav","ext_throw_javelin_05.wav","ext_throw_javelin_06.wav","ext_throw_javelin_07.wav","ext_throw_javelin_08.wav"]),
# ("throw_javelin",						sf_vol_5,													["min_throw_javelin_01.wav"]),
 ("throw_axe",							sf_vol_7,													["min_throw_axe_01.wav"]),
 ("throw_knife",						sf_vol_5,													["min_throw_knife_01.wav","ext_throw_knife_02.wav","ext_throw_knife_03.wav","ext_throw_knife_04.wav","ext_throw_knife_05.wav"]),
# ("throw_knife",						sf_vol_5,													["min_throw_knife_01.wav"]),
 ("throw_stone",						sf_vol_5,													["min_throw_stone_01.wav","ext_throw_stone_02.wav","ext_throw_stone_03.wav","ext_throw_stone_04.wav"]),
# ("throw_stone",						sf_vol_5,													["min_throw_stone_01.wav"]),

#Reload
 ("reload_crossbow",					sf_vol_3,													["min_pull_crossbow_string_01.wav","ext_pull_crossbow_string_02.wav","ext_pull_crossbow_string_03.wav","ext_pull_crossbow_string_04.wav","ext_pull_crossbow_string_05.wav","ext_pull_crossbow_string_06.wav","ext_pull_crossbow_string_07.wav","ext_pull_crossbow_string_08.wav"]),
# ("reload_crossbow",					sf_vol_3,													["min_pull_crossbow_string_01.wav"]),
 ("reload_crossbow_continue",			sf_vol_6,													["min_crossbow_load_01.wav","ext_crossbow_load_02.wav","ext_crossbow_load_03.wav","ext_crossbow_load_04.wav","ext_crossbow_load_05.wav","ext_crossbow_load_06.wav","ext_crossbow_load_07.wav","ext_crossbow_load_08.wav"]),
# ("reload_crossbow_continue",			sf_vol_6,													["min_crossbow_load_01.wav"]),
 ("pull_bow",							sf_vol_6,													["min_pull_bow_string_01.wav","pull_bow_string_02.wav","ext_pull_bow_string_03.wav","ext_pull_bow_string_04.wav","ext_pull_bow_string_05.wav","ext_pull_bow_string_06.wav","ext_pull_bow_string_07.wav","ext_pull_bow_string_08.wav"]),
# ("pull_bow",							sf_vol_6,													["min_pull_bow_string_01.wav"]),
 ("pull_arrow",							sf_vol_5,													["min_draw_arrow_01.wav","ext_draw_arrow_02.wav","ext_draw_arrow_03.wav","ext_draw_arrow_04.wav","ext_draw_arrow_05.wav","ext_draw_arrow_06.wav","ext_draw_arrow_07.wav","ext_draw_arrow_08.wav"]),
# ("pull_arrow",						sf_vol_5,													["min_draw_arrow_01.wav"]),

#Ranged passing by
 ("arrow_pass_by",						0,															["min_arrow_pass_01.wav","min_arrow_pass_02.wav","min_arrow_pass_03.wav","min_arrow_pass_04.wav","ext_arrow_pass_05.wav","ext_arrow_pass_06.wav","ext_arrow_pass_07.wav","ext_arrow_pass_08.wav","ext_arrow_pass_09.wav","ext_arrow_pass_10.wav","ext_arrow_pass_11.wav","ext_arrow_pass_12.wav","ext_arrow_pass_13.wav"]),
# ("arrow_pass_by",						0,															["min_arrow_pass_01.wav","min_arrow_pass_02.wav","min_arrow_pass_03.wav","min_arrow_pass_04.wav"]),
 ("bolt_pass_by",						0,															["min_bolt_pass_01.wav","ext_bolt_pass_02.wav","ext_bolt_pass_03.wav","ext_bolt_pass_04.wav","ext_bolt_pass_05.wav","ext_bolt_pass_06.wav","ext_bolt_pass_07.wav","ext_bolt_pass_08.wav","ext_bolt_pass_09.wav","ext_bolt_pass_10.wav"]),
# ("bolt_pass_by",						0,															["min_bolt_pass_01.wav"]),
 ("javelin_pass_by",					0,															["min_javelin_pass_by_01.wav","min_javelin_pass_by_02.wav","ext_javelin_pass_by_03.wav","ext_javelin_pass_by_04.wav","ext_javelin_pass_by_05.wav","ext_javelin_pass_by_06.wav","ext_javelin_pass_by_07.wav","ext_javelin_pass_by_08.wav"]),
# ("javelin_pass_by",					0,															["min_javelin_pass_by_01.wav","min_javelin_pass_by_02.wav"]),
 ("stone_pass_by",						sf_vol_9,													["min_stone_pass_01.wav","ext_stone_pass_02.wav","ext_stone_pass_03.wav","ext_stone_pass_04.wav"]),
# ("stone_pass_by",						sf_vol_9,													["min_stone_pass_01.wav"]),
 ("axe_pass_by",						0,															["min_axe_pass_by_01.wav","ext_axe_pass_by_02.wav"]),
# ("axe_pass_by",						0,															["min_axe_pass_by_01.wav"]),
 ("knife_pass_by",						0,															["min_knife_pass_01.wav","ext_knife_pass_02.wav","ext_knife_pass_03.wav","ext_knife_pass_04.wav","ext_knife_pass_05.wav"]),
# ("knife_pass_by",						0,															["min_knife_pass_01.wav"]),
 ("bullet_pass_by",						0,															["min_bullet_pass_01.wav","ext_bullet_pass_02.wav","ext_bullet_pass_03.wav","ext_bullet_pass_04.wav","ext_bullet_pass_05.wav","ext_bullet_pass_06.wav","ext_bullet_pass_07.wav","ext_bullet_pass_08.wav","ext_bullet_pass_09.wav","ext_bullet_pass_10.wav","ext_bullet_pass_11.wav","ext_bullet_pass_12.wav"]),
# ("bullet_pass_by",					0,															["min_bullet_pass_01.wav"]),

#Ranged Incoming
 ("incoming_arrow_hit_ground",			sf_priority_7|sf_vol_7,										["min_arrow_ground_01.wav","min_arrow_ground_02.wav","min_arrow_ground_03.wav","ext_arrow_ground_04.wav","ext_arrow_ground_05.wav","ext_arrow_ground_06.wav","ext_arrow_ground_07.wav","ext_arrow_ground_08.wav"]),
# ("incoming_arrow_hit_ground",			sf_priority_7|sf_vol_7,										["min_arrow_ground_01.wav","min_arrow_ground_02.wav","min_arrow_ground_03.wav"]),
 ("incoming_bolt_hit_ground",			sf_priority_7|sf_vol_7,										["min_bolt_ground_01.wav","min_bolt_ground_02.wav","min_bolt_ground_03.wav","ext_bolt_ground_04.wav","ext_bolt_ground_05.wav","ext_bolt_ground_06.wav","ext_bolt_ground_07.wav","ext_bolt_ground_08.wav"]),
# ("incoming_bolt_hit_ground",			sf_priority_7|sf_vol_7,										["min_bolt_ground_01.wav","min_bolt_ground_02.wav","min_bolt_ground_03.wav"]),
 ("incoming_javelin_hit_ground",		sf_priority_7|sf_vol_7,										["min_javelin_ground_01.wav","ext_javelin_ground_02.wav","ext_javelin_ground_03.wav","ext_javelin_ground_04.wav","ext_javelin_ground_05.wav","ext_javelin_ground_06.wav","ext_javelin_ground_07.wav","ext_javelin_ground_08.wav"]),
# ("incoming_javelin_hit_ground",		sf_priority_7|sf_vol_7,										["min_javelin_ground_01.wav"]),
 ("incoming_stone_hit_ground",			sf_priority_7|sf_vol_7,										["min_stone_ground_01.wav","ext_stone_ground_02.wav"]),
# ("incoming_stone_hit_ground",			sf_priority_7|sf_vol_7,										["min_stone_ground_01.wav"]),
 ("incoming_axe_hit_ground",			sf_priority_7|sf_vol_7,										["min_axe_ground_01.wav","ext_axe_ground_02.wav"]),
# ("incoming_axe_hit_ground",			sf_priority_7|sf_vol_7,										["min_axe_ground_01.wav"]),
 ("incoming_knife_hit_ground",			sf_priority_7|sf_vol_7,										["min_knife_ground_01.wav","ext_knife_ground_02.wav"]),
# ("incoming_knife_hit_ground",			sf_priority_7|sf_vol_7,										["min_knife_ground_01.wav"]),
 ("incoming_bullet_hit_ground",			sf_priority_7|sf_vol_7,										["min_bullet_ground_01.wav","ext_bullet_ground_02.wav","ext_bullet_ground_03.wav","ext_bullet_ground_04.wav","ext_bullet_ground_05.wav"]),
# ("incoming_bullet_hit_ground",		sf_priority_7|sf_vol_7,										["min_bullet_ground_01.wav"]),

#Ranged Outgoing
 ("outgoing_arrow_hit_ground",			sf_priority_7|sf_vol_7,										["min_arrow_ground_09.wav","min_arrow_ground_10.wav","min_arrow_ground_11.wav","ext_arrow_ground_12.wav","ext_arrow_ground_13.wav","ext_arrow_ground_14.wav","ext_arrow_ground_15.wav","ext_arrow_ground_16.wav"]),
# ("outgoing_arrow_hit_ground",			sf_priority_7|sf_vol_7,										["min_arrow_ground_09.wav","min_arrow_ground_10.wav","min_arrow_ground_11.wav"]),
 ("outgoing_bolt_hit_ground",			sf_priority_7|sf_vol_7,										["min_bolt_ground_09.wav","min_bolt_ground_10.wav","min_bolt_ground_11.wav","ext_bolt_ground_12.wav","ext_bolt_ground_13.wav","ext_bolt_ground_14.wav","ext_bolt_ground_15.wav","ext_bolt_ground_16.wav"]),
# ("outgoing_bolt_hit_ground",			sf_priority_7|sf_vol_7,										["min_bolt_ground_09.wav","min_bolt_ground_10.wav","min_bolt_ground_11.wav"]),
 ("outgoing_javelin_hit_ground",		sf_priority_7|sf_vol_10,									["min_javelin_ground_09.wav","ext_javelin_ground_10.wav","ext_javelin_ground_11.wav","ext_javelin_ground_12.wav","ext_javelin_ground_13.wav","javelin_ground_14.wav","ext_javelin_ground_15.wav","ext_javelin_ground_16.wav"]),
# ("outgoing_javelin_hit_ground",		sf_priority_7|sf_vol_10,									["min_javelin_ground_09.wav"]),
 ("outgoing_stone_hit_ground",			sf_priority_7|sf_vol_7,										["min_stone_ground_03.wav","ext_stone_ground_04.wav"]),
# ("outgoing_stone_hit_ground",			sf_priority_7|sf_vol_7,										["min_stone_ground_03.wav"]),
 ("outgoing_axe_hit_ground",			sf_priority_7|sf_vol_7,										["min_axe_ground_03.wav"]),
 ("outgoing_knife_hit_ground",			sf_priority_7|sf_vol_7,										["min_knife_ground_03.wav"]),
 ("outgoing_bullet_hit_ground",			sf_priority_7|sf_vol_7,										["min_bullet_ground_06.wav","ext_bullet_ground_07.wav","ext_bullet_ground_08.wav","ext_bullet_ground_09.wav"]),
# ("outgoing_bullet_hit_ground",		sf_priority_7|sf_vol_7,										["min_bullet_ground_06.wav"]),

#Draw and put back weapons
 ("draw_sword",							sf_priority_4,												["min_draw_sword_01.wav","ext_draw_sword_02.wav","ext_draw_sword_03.wav","ext_draw_sword_04.wav","ext_draw_sword_05.wav","ext_draw_sword_06.wav","ext_draw_sword_07.wav","ext_draw_sword_08.wav"]),
# ("draw_sword",						sf_priority_4,												["min_draw_sword_01.wav"]),
 ("put_back_sword",						sf_priority_4,												["min_put_away_sword_01.wav","ext_put_away_sword_02.wav","ext_put_away_sword_03.wav","ext_put_away_sword_04.wav","ext_put_away_sword_05.wav","ext_put_away_sword_06.wav","ext_put_away_sword_07.wav","ext_put_away_sword_08.wav"]),
# ("put_back_sword",					sf_priority_4,												["min_put_away_sword_01.wav"]),
 ("draw_greatsword",					sf_priority_4,												["min_draw_greatsword_01.wav","ext_draw_greatsword_02.wav"]),
# ("draw_greatsword",					sf_priority_4,												["min_draw_greatsword_01.wav"]),
 ("put_back_greatsword",				sf_priority_4,												["min_put_away_greatsword_01.wav"]),
 ("draw_axe",							sf_priority_4,												["min_draw_axe_01.wav","ext_draw_axe_02.wav"]),
# ("draw_axe",							sf_priority_4,												["min_draw_axe_01.wav"]),
 ("put_back_axe",						sf_priority_4,												["min_put_away_axe_01.wav"]),
 ("draw_greataxe",						sf_priority_4,												["min_draw_greataxe_01.wav","ext_draw_greataxe_02.wav","ext_draw_greataxe_03.wav"]),
# ("draw_greataxe",						sf_priority_4,												["min_draw_greataxe_01.wav"]),
 ("put_back_greataxe",					sf_priority_4,												["min_put_away_greataxe_01.wav"]),
 ("draw_spear",							sf_priority_4,												["min_draw_spear_01.wav","ext_draw_spear_02.wav","ext_draw_spear_03.wav","ext_draw_spear_04.wav"]),
# ("draw_spear",						sf_priority_4,												["min_draw_spear_01.wav"]),
 ("put_back_spear",						sf_priority_4,												["min_put_away_spear_01.wav"]),
 ("draw_crossbow",						sf_priority_4|sf_vol_6,										["min_draw_crossbow_01.wav","ext_draw_crossbow_02.wav","ext_draw_crossbow_03.wav"]),
# ("draw_crossbow",						sf_priority_4|sf_vol_6,										["min_draw_crossbow_01.wav"]),
 ("put_back_crossbow",					sf_priority_4,												["min_put_away_crossbow_01.wav"]),
 ("draw_revolver",						sf_priority_4,												["min_draw_from_holster.wav"]),
 ("put_back_revolver",					sf_priority_4,												["min_put_back_to_holster.wav"]),
 ("draw_dagger",						sf_priority_4,												["min_draw_dagger_01.wav","ext_draw_dagger_02.wav","ext_draw_dagger_03.wav"]),
# ("draw_dagger",						sf_priority_4,												["min_draw_dagger_01.wav"]),
 ("put_back_dagger",					sf_priority_4,												["min_put_away_dagger_01.wav"]),
 ("draw_bow",							sf_priority_4,												["min_draw_bow_01.wav","ext_draw_bow_02.wav","ext_draw_bow_03.wav"]),
# ("draw_bow",							sf_priority_4,												["min_draw_bow_01.wav"]),
 ("put_back_bow",						sf_priority_4,												["min_put_away_bow_01.wav"]),
 ("draw_shield",						sf_priority_4|sf_vol_7,										["min_draw_shield_01.wav","ext_draw_shield_02.wav","ext_draw_shield_03.wav","ext_draw_shield_04.wav","ext_draw_shield_05.wav","ext_draw_shield_06.wav","ext_draw_shield_07.wav","ext_draw_shield_08.wav"]),
# ("draw_shield",						sf_priority_4|sf_vol_7,										["min_draw_shield_01.wav"]),
 ("put_back_shield",					sf_priority_4|sf_vol_7,										["min_put_away_shield_01.wav"]),
 ("draw_other",							sf_priority_4,												["min_draw_weapon_01.wav","ext_draw_weapon_02.wav","ext_draw_weapon_03.wav","ext_draw_weapon_04.wav","ext_draw_weapon_05.wav","ext_draw_weapon_06.wav","ext_draw_weapon_07.wav","ext_draw_weapon_08.wav"]),
# ("draw_other",						sf_priority_4,												["min_draw_weapon_01.wav"]),
 ("put_back_other",						sf_priority_4,												["min_put_away_weapon_01.wav","ext_put_away_weapon_02.wav","ext_put_away_shi_weapon_03.wav","ext_put_away_weapon_04.wav","ext_put_away_weapon_05.wav","ext_put_away_weapon_06.wav","ext_put_away_weapon_07.wav","ext_put_away_weapon_08.wav"]),
# ("put_back_other",					sf_priority_4,												["min_put_away_weapon_01.wav"]),

#Falling bodies
 ("body_fall_small",					sf_priority_6|sf_vol_10,									["min_body_fall_small_01.wav","min_body_fall_small_02.wav","ext_body_fall_small_03.wav","ext_body_fall_small_04.wav","ext_body_fall_small_05.wav","ext_body_fall_small_06.wav","ext_body_fall_small_07.wav","ext_body_fall_small_08.wav","ext_body_fall_small_09.wav","ext_body_fall_small_10.wav"]),
# ("body_fall_small",					sf_priority_6|sf_vol_10,									["min_body_fall_small_01.wav","min_body_fall_small_02.wav"]),
 ("body_fall_big",						sf_priority_6|sf_vol_10,									["min_body_fall_large_01.wav","min_body_fall_large_02.wav","ext_body_fall_large_03.wav","ext_body_fall_large_04.wav","ext_body_fall_large_05.wav","ext_body_fall_large_06.wav","ext_body_fall_large_07.wav","ext_body_fall_large_08.wav"]),
# ("body_fall_big",						sf_priority_6|sf_vol_10,									["min_body_fall_large_01.wav","min_body_fall_large_02.wav"]),
 ("horse_body_fall_begin",				sf_priority_7|sf_vol_10,									["min_horse_fall_b_01.wav","min_horse_fall_b_02.wav","ext_horse_fall_b_03.wav","ext_horse_fall_b_04.wav"]),
# ("horse_body_fall_begin",				sf_priority_7|sf_vol_10,									["min_horse_fall_b_01.wav","min_horse_fall_b_02.wav"]),
 ("horse_body_fall_end",				sf_priority_7|sf_vol_10,									["min_horse_fall_e_01.wav","min_horse_fall_e_02.wav","ext_horse_fall_e_03.wav","ext_horse_fall_e_04.wav"]),
# ("horse_body_fall_end",				sf_priority_7|sf_vol_10,									["min_horse_fall_e_01.wav","min_horse_fall_e_02.wav"]),

#Hit on weapons and shields
 ("hit_wood_wood",						sf_priority_7|sf_vol_10,									["min_hit_wood_wood_01.wav","min_hit_wood_wood_02.wav","min_hit_wood_wood_03.wav","min_hit_wood_wood_04.wav","min_hit_wood_wood_05.wav","min_hit_wood_wood_06.wav","min_hit_wood_wood_07.wav","ext_hit_wood_wood_08.wav","ext_hit_wood_wood_09.wav","ext_hit_wood_wood_10.wav","ext_hit_wood_wood_11.wav","ext_hit_wood_wood_12.wav","ext_hit_wood_wood_13.wav","ext_hit_wood_wood_14.wav","ext_hit_wood_wood_15.wav","ext_hit_wood_wood_16.wav"]),
# ("hit_wood_wood",						sf_priority_7|sf_vol_10,									["min_hit_wood_wood_01.wav","min_hit_wood_wood_02.wav","min_hit_wood_wood_03.wav","min_hit_wood_wood_04.wav","min_hit_wood_wood_05.wav","min_hit_wood_wood_06.wav","min_hit_wood_wood_07.wav"]),
 ("hit_metal_metal",					sf_priority_7|sf_vol_10,									["min_hit_metal_metal_01.wav","min_hit_metal_metal_02.wav","min_hit_metal_metal_03.wav","min_hit_metal_metal_04.wav","min_hit_metal_metal_05.wav","min_hit_metal_metal_06.wav","min_hit_metal_metal_07.wav","min_hit_metal_metal_08.wav","min_hit_metal_metal_09.wav","min_hit_metal_metal_10.wav","ext_hit_metal_metal_11.wav","ext_hit_metal_metal_12.wav","ext_hit_metal_metal_13.wav","ext_hit_metal_metal_14.wav","ext_hit_metal_metal_15.wav","ext_hit_metal_metal_16.wav","ext_hit_metal_metal_17.wav","ext_hit_metal_metal_18.wav","ext_hit_metal_metal_19.wav","ext_hit_metal_metal_20.wav"]),
# ("hit_metal_metal",					sf_priority_7|sf_vol_10,									["min_hit_metal_metal_01.wav","min_hit_metal_metal_02.wav","min_hit_metal_metal_03.wav","min_hit_metal_metal_04.wav","min_hit_metal_metal_05.wav","min_hit_metal_metal_06.wav","min_hit_metal_metal_07.wav","min_hit_metal_metal_08.wav","min_hit_metal_metal_09.wav","min_hit_metal_metal_10.wav"]),
 ("hit_wood_metal",						sf_priority_7|sf_vol_10,									["min_hit_wood_metal_01.wav","min_hit_wood_metal_02.wav","min_hit_wood_metal_03.wav","ext_hit_wood_metal_04.wav","ext_hit_wood_metal_05.wav","ext_hit_wood_metal_06.wav","ext_hit_wood_metal_07.wav","ext_hit_wood_metal_08.wav","ext_hit_wood_metal_09.wav","ext_hit_wood_metal_10.wav","ext_hit_wood_metal_11.wav","ext_hit_wood_metal_12.wav","ext_hit_wood_metal_13.wav","ext_hit_wood_metal_14.wav","ext_hit_wood_metal_15.wav","ext_hit_wood_metal_16.wav","ext_hit_wood_metal_17.wav","ext_hit_wood_metal_18.wav"]),
# ("hit_wood_metal",					sf_priority_7|sf_vol_10,									["min_hit_wood_metal_01.wav","min_hit_wood_metal_02.wav","min_hit_wood_metal_03.wav"]),
 ("shield_hit_wood_wood",				sf_priority_7|sf_vol_10,									["min_shield_hit_wood_wood_01.wav","min_shield_hit_wood_wood_02.wav","min_shield_hit_wood_wood_03.wav","ext_shield_hit_wood_wood_04.wav","ext_shield_hit_wood_wood_05.wav","ext_shield_hit_wood_wood_06.wav","ext_shield_hit_wood_wood_07.wav","ext_shield_hit_wood_wood_08.wav","ext_shield_hit_wood_wood_09.wav","ext_shield_hit_wood_wood_10.wav","ext_shield_hit_wood_wood_11.wav","ext_shield_hit_wood_wood_12.wav","ext_shield_hit_wood_wood_13.wav","ext_shield_hit_wood_wood_14.wav","ext_shield_hit_wood_wood_15.wav","ext_shield_hit_wood_wood_16.wav"]),
# ("shield_hit_wood_wood",				sf_priority_7|sf_vol_10,									["min_shield_hit_wood_wood_01.wav","min_shield_hit_wood_wood_02.wav","min_shield_hit_wood_wood_03.wav"]),
 ("shield_hit_metal_metal",				sf_priority_7|sf_vol_10,									["min_shield_hit_metal_metal_01.wav","min_shield_hit_metal_metal_02.wav","min_shield_hit_metal_metal_03.wav","min_shield_hit_metal_metal_04.wav","ext_shield_hit_metal_metal_05.wav","ext_shield_hit_metal_metal_06.wav","ext_shield_hit_metal_metal_07.wav","ext_shield_hit_metal_metal_08.wav","ext_shield_hit_metal_metal_09.wav","ext_shield_hit_metal_metal_10.wav","ext_shield_hit_metal_metal_11.wav","ext_shield_hit_metal_metal_12.wav","ext_shield_hit_metal_metal_13.wav","ext_shield_hit_metal_metal_14.wav","ext_shield_hit_metal_metal_15.wav","ext_shield_hit_metal_metal_16.wav"]),
# ("shield_hit_metal_metal",			sf_priority_7|sf_vol_10,									["min_shield_hit_metal_metal_01.wav","min_shield_hit_metal_metal_02.wav","min_shield_hit_metal_metal_03.wav","min_shield_hit_metal_metal_04.wav"]),
 ("shield_hit_wood_metal",				sf_priority_7|sf_vol_10,									["min_shield_hit_wood_metal_01.wav","min_shield_hit_wood_metal_02.wav","min_shield_hit_wood_metal_03.wav","min_shield_hit_wood_metal_04.wav","ext_shield_hit_wood_metal_05.wav","ext_shield_hit_wood_metal_06.wav","ext_shield_hit_wood_metal_07.wav","ext_shield_hit_wood_metal_08.wav","ext_shield_hit_wood_metal_09.wav","ext_shield_hit_wood_metal_10.wav","ext_shield_hit_wood_metal_11.wav","ext_shield_hit_wood_metal_12.wav","ext_shield_hit_wood_metal_13.wav","ext_shield_hit_wood_metal_14.wav","ext_shield_hit_wood_metal_15.wav","ext_shield_hit_wood_metal_16.wav"]), #(shield is wood)
# ("shield_hit_wood_metal",				sf_priority_7|sf_vol_10,									["min_shield_hit_wood_metal_01.wav","min_shield_hit_wood_metal_02.wav","min_shield_hit_wood_metal_03.wav","min_shield_hit_wood_metal_04.wav"]), #(shield is wood)
 ("shield_hit_metal_wood",				sf_priority_7|sf_vol_10,									["min_shield_hit_metal_wood_01.wav","min_shield_hit_metal_wood_02.wav","min_shield_hit_metal_wood_03.wav","min_shield_hit_metal_wood_04.wav","ext_shield_hit_metal_wood_05.wav","ext_shield_hit_metal_wood_06.wav","ext_shield_hit_metal_wood_07.wav","ext_shield_hit_metal_wood_08.wav","ext_shield_hit_metal_wood_09.wav","ext_shield_hit_metal_wood_10.wav","ext_shield_hit_metal_wood_11.wav","ext_shield_hit_metal_wood_12.wav","ext_shield_hit_metal_wood_13.wav","ext_shield_hit_metal_wood_14.wav","ext_shield_hit_metal_wood_15.wav","ext_shield_hit_metal_wood_16.wav"]),#(shield is metal)
# ("shield_hit_metal_wood",				sf_priority_7|sf_vol_10,									["min_shield_hit_metal_wood_01.wav","min_shield_hit_metal_wood_02.wav","min_shield_hit_metal_wood_03.wav","min_shield_hit_metal_wood_04.wav"]),#(shield is metal)
 ("shield_broken",						sf_priority_9,												["min_shield_break_01.wav","ext_shield_break_02.wav"]),
# ("shield_broken",						sf_priority_9,												["min_shield_break_01.wav"]),

#People getting hit and die
 ("man_hit",							sf_priority_2|sf_vol_10,									["min_man_grunt_pain_01.wav","min_man_grunt_pain_02.wav","min_man_grunt_pain_03.wav","min_man_grunt_pain_04.wav","min_man_grunt_pain_05.wav","min_man_grunt_pain_06.wav","min_man_grunt_pain_07.wav","min_man_grunt_pain_08.wav","min_man_grunt_pain_09.wav","min_man_grunt_pain_10.wav","min_man_grunt_pain_11.wav","min_man_grunt_pain_12.wav","min_man_grunt_pain_13.wav","min_man_grunt_pain_14.wav","min_man_grunt_pain_15.wav","min_man_grunt_pain_16.wav","min_man_grunt_pain_17.wav","min_man_grunt_pain_18.wav","min_man_grunt_pain_19.wav","min_man_grunt_pain_20.wav","ext_man_grunt_pain_21.wav","ext_man_grunt_pain_22.wav","ext_man_grunt_pain_23.wav","ext_man_grunt_pain_24.wav","ext_man_grunt_pain_25.wav","ext_man_grunt_pain_26.wav","ext_man_grunt_pain_27.wav","ext_man_grunt_pain_28.wav","ext_man_grunt_pain_29.wav","ext_man_grunt_pain_30.wav","ext_man_grunt_pain_31.wav","ext_man_grunt_pain_32.wav"]),
# ("man_hit",							sf_priority_2|sf_vol_10,									["min_man_grunt_pain_01.wav","min_man_grunt_pain_02.wav","min_man_grunt_pain_03.wav","min_man_grunt_pain_04.wav","min_man_grunt_pain_05.wav","min_man_grunt_pain_06.wav","min_man_grunt_pain_07.wav","min_man_grunt_pain_08.wav","min_man_grunt_pain_09.wav","min_man_grunt_pain_10.wav","min_man_grunt_pain_11.wav","min_man_grunt_pain_12.wav","min_man_grunt_pain_13.wav","min_man_grunt_pain_14.wav","min_man_grunt_pain_15.wav","min_man_grunt_pain_16.wav","min_man_grunt_pain_17.wav","min_man_grunt_pain_18.wav","min_man_grunt_pain_19.wav","min_man_grunt_pain_20.wav"]),
 ("man_die",							sf_priority_10|sf_vol_10,									["min_man_die_01.wav","min_man_die_02.wav","min_man_die_03.wav","min_man_die_04.wav","min_man_die_05.wav","min_man_die_06.wav","min_man_die_07.wav","min_man_die_08.wav","min_man_die_09.wav","min_man_die_10.wav","min_man_die_11.wav","min_man_die_12.wav","min_man_die_13.wav","min_man_die_14.wav","ext_man_die_15.wav","ext_man_die_16.wav","ext_man_die_17.wav","ext_man_die_18.wav","ext_man_die_19.wav","ext_man_die_20.wav","ext_man_die_21.wav","ext_man_die_22.wav","ext_man_die_23.wav","ext_man_die_24.wav","ext_man_die_25.wav","ext_man_die_26.wav","ext_man_die_27.wav","ext_man_die_28.wav","ext_man_die_29.wav","ext_man_die_30.wav","ext_man_die_31.wav","ext_man_die_32.wav"]),
# ("man_die",							sf_priority_10|sf_vol_10,									["min_man_die_01.wav","min_man_die_02.wav","min_man_die_03.wav","min_man_die_04.wav","min_man_die_05.wav","min_man_die_06.wav","min_man_die_07.wav","min_man_die_08.wav","min_man_die_09.wav","min_man_die_10.wav","min_man_die_11.wav","min_man_die_12.wav","min_man_die_13.wav","min_man_die_14.wav"]),
 ("woman_hit",							sf_priority_3,												["min_woman_hit_01.wav","min_woman_hit_02.wav","min_woman_hit_03.wav","min_woman_hit_04.wav","min_woman_hit_05.wav","min_woman_hit_06.wav","min_woman_hit_07.wav","min_woman_hit_08.wav","min_woman_hit_09.wav","min_woman_hit_10.wav","ext_woman_hit_11.wav"]),
# ("woman_hit",							sf_priority_3,												["min_woman_hit_01.wav","min_woman_hit_02.wav","min_woman_hit_03.wav","min_woman_hit_04.wav","min_woman_hit_05.wav","min_woman_hit_06.wav","min_woman_hit_07.wav","min_woman_hit_08.wav","min_woman_hit_09.wav","min_woman_hit_10.wav"]),
 ("woman_die",							sf_priority_10,												["min_woman_die_01.wav"]),
 ("woman_yell",							sf_priority_10|sf_vol_10,									["min_woman_yell_01.wav","min_woman_yell_02.wav"]),

#Other sounds
 ("hide",								0,															["min_hide.wav"]),
 ("unhide",								0,															["min_unhide.wav"]),
 ("neigh",								0,															["min_horse_exterior_whinny_01.wav","min_horse_exterior_whinny_02.wav","min_horse_exterior_whinny_03.wav","min_horse_exterior_whinny_04.wav","min_horse_exterior_whinny_05.wav","min_horse_exterior_whinny_06.wav","ext_horse_exterior_whinny_07.wav","ext_horse_exterior_whinny_08.wav","ext_horse_exterior_whinny_09.wav"]),
# ("neigh",								0,															["min_horse_exterior_whinny_01.wav","min_horse_exterior_whinny_02.wav","min_horse_exterior_whinny_03.wav","min_horse_exterior_whinny_04.wav","min_horse_exterior_whinny_05.wav","min_horse_exterior_whinny_06.wav"]),
 ("gallop",								sf_vol_3,													["min_gallop_01.wav","min_gallop_02.wav","min_gallop_03.wav","ext_gallop_04.wav","ext_gallop_05.wav","ext_gallop_06.wav","ext_gallop_07.wav"]),
# ("gallop",							sf_vol_3,													["min_gallop_01.wav","min_gallop_02.wav","min_gallop_03.wav"]),
 ("battle",								sf_vol_4,													["min_battle.wav"]),

#Armor gets hit
 ("arrow_hit_body",						sf_priority_4,												["min_missile_flesh_01.wav","min_missile_flesh_02.wav","min_missile_flesh_03.wav","ext_missile_flesh_04.wav","ext_missile_flesh_05.wav","ext_missile_flesh_06.wav","ext_missile_flesh_07.wav","ext_missile_flesh_08.wav"]),
# ("arrow_hit_body",					sf_priority_4,												["min_missile_flesh_01.wav","min_missile_flesh_02.wav","min_missile_flesh_03.wav"]),
 ("metal_hit_low_armor_low_damage",		sf_priority_5|sf_vol_9,										["min_metal_low_low_01.wav","min_metal_low_low_02.wav","min_metal_low_low_03.wav","ext_metal_low_low_04.wav","ext_metal_low_low_05.wav","ext_metal_low_low_06.wav","ext_metal_low_low_07.wav","ext_metal_low_low_08.wav","ext_metal_low_low_09.wav","ext_metal_low_low_10.wav","ext_metal_low_low_11.wav","ext_metal_low_low_12.wav","ext_metal_low_low_13.wav","ext_metal_low_low_14.wav","ext_metal_low_low_15.wav","ext_metal_low_low_16.wav"]),
# ("metal_hit_low_armor_low_damage",	sf_priority_5|sf_vol_9,										["min_metal_low_low_01.wav","min_metal_low_low_02.wav","min_metal_low_low_03.wav"]),
 ("metal_hit_low_armor_high_damage",	sf_priority_5|sf_vol_9,										["min_metal_low_high_01.wav","min_metal_low_high_02.wav","min_metal_low_high_03.wav","ext_metal_low_high_04.wav","ext_metal_low_high_05.wav","ext_metal_low_high_06.wav","ext_metal_low_high_07.wav","ext_metal_low_high_08.wav","ext_metal_low_high_09.wav","ext_metal_low_high_10.wav","ext_metal_low_high_11.wav","ext_metal_low_high_12.wav","ext_metal_low_high_13.wav","ext_metal_low_high_14.wav","ext_metal_low_high_15.wav","ext_metal_low_high_16.wav"]),
# ("metal_hit_low_armor_high_damage",	sf_priority_5|sf_vol_9,										["min_metal_low_high_01.wav","min_metal_low_high_02.wav","min_metal_low_high_03.wav"]),
 ("metal_hit_high_armor_low_damage",	sf_priority_5|sf_vol_9,										["min_metal_high_low_01.wav","min_metal_high_low_02.wav","min_metal_high_low_03.wav","ext_metal_high_low_04.wav","ext_metal_high_low_05.wav","ext_metal_high_low_06.wav","ext_metal_high_low_07.wav","ext_metal_high_low_08.wav","ext_metal_high_low_09.wav","ext_metal_high_low_10.wav","ext_metal_high_low_11.wav","ext_metal_high_low_12.wav","ext_metal_high_low_13.wav","ext_metal_high_low_14.wav","ext_metal_high_low_15.wav","ext_metal_high_low_16.wav"]),
# ("metal_hit_high_armor_low_damage",	sf_priority_5|sf_vol_9,										["min_metal_high_low_01.wav","min_metal_high_low_02.wav","min_metal_high_low_03.wav"]),
 ("metal_hit_high_armor_high_damage",	sf_priority_5|sf_vol_9,										["min_metal_high_high_01.wav","min_metal_high_high_02.wav","min_metal_high_high_03.wav","ext_metal_high_high_04.wav","ext_metal_high_high_05.wav","ext_metal_high_high_06.wav","ext_metal_high_high_07.wav","ext_metal_high_high_08.wav","ext_metal_high_high_09.wav","ext_metal_high_high_10.wav","ext_metal_high_high_11.wav","ext_metal_high_high_12.wav","ext_metal_high_high_13.wav","ext_metal_high_high_14.wav","ext_metal_high_high_15.wav","ext_metal_high_high_16.wav"]),
# ("metal_hit_high_armor_high_damage",	sf_priority_5|sf_vol_9,										["min_metal_high_high_01.wav","min_metal_high_high_02.wav","min_metal_high_high_03.wav"]),
 ("wooden_hit_low_armor_low_damage",	sf_priority_5|sf_vol_9,										["min_blunt_low_low_01.wav","min_blunt_low_low_02.wav","min_blunt_low_low_03.wav","ext_blunt_low_low_04.wav","ext_blunt_low_low_05.wav","ext_blunt_low_low_06.wav","ext_blunt_low_low_07.wav","ext_blunt_low_low_08.wav","ext_blunt_low_low_09.wav","ext_blunt_low_low_10.wav","ext_blunt_low_low_11.wav","ext_blunt_low_low_12.wav","ext_blunt_low_low_13.wav","ext_blunt_low_low_14.wav","ext_blunt_low_low_15.wav","ext_blunt_low_low_16.wav"]),
# ("wooden_hit_low_armor_low_damage",	sf_priority_5|sf_vol_9,										["min_blunt_low_low_01.wav","min_blunt_low_low_02.wav","min_blunt_low_low_03.wav"]),
 ("wooden_hit_low_armor_high_damage",	sf_priority_5|sf_vol_9,										["min_blunt_low_high_01.wav","min_blunt_low_high_02.wav","min_blunt_low_high_03.wav","ext_blunt_low_high_04.wav","ext_blunt_low_high_05.wav","ext_blunt_low_high_06.wav","ext_blunt_low_high_07.wav","ext_blunt_low_high_08.wav","ext_blunt_low_high_09.wav","ext_blunt_low_high_10.wav","ext_blunt_low_high_11.wav","ext_blunt_low_high_12.wav","ext_blunt_low_high_13.wav","ext_blunt_low_high_14.wav","ext_blunt_low_high_15.wav","ext_blunt_low_high_16.wav"]),
# ("wooden_hit_low_armor_high_damage",	sf_priority_5|sf_vol_9,										["min_blunt_low_high_01.wav","min_blunt_low_high_02.wav","min_blunt_low_high_03.wav"]),
 ("wooden_hit_high_armor_low_damage",	sf_priority_5|sf_vol_9,										["min_blunt_high_low_01.wav","min_blunt_high_low_02.wav","min_blunt_high_low_03.wav","ext_blunt_high_low_04.wav","ext_blunt_high_low_05.wav","ext_blunt_high_low_06.wav","ext_blunt_high_low_07.wav","ext_blunt_high_low_08.wav","ext_blunt_high_low_09.wav","ext_blunt_high_low_10.wav","ext_blunt_high_low_11.wav","ext_blunt_high_low_12.wav","ext_blunt_high_low_13.wav","ext_blunt_high_low_14.wav","ext_blunt_high_low_15.wav","ext_blunt_high_low_16.wav"]),
# ("wooden_hit_high_armor_low_damage",	sf_priority_5|sf_vol_9,										["min_blunt_high_low_01.wav","min_blunt_high_low_02.wav","min_blunt_high_low_03.wav"]),
 ("wooden_hit_high_armor_high_damage",	sf_priority_5|sf_vol_9,										["min_blunt_high_high_01.wav","min_blunt_high_high_02.wav","min_blunt_high_high_03.wav","ext_blunt_high_high_04.wav","ext_blunt_high_high_05.wav","ext_blunt_high_high_06.wav","ext_blunt_high_high_07.wav","ext_blunt_high_high_08.wav","ext_blunt_high_high_09.wav","ext_blunt_high_high_10.wav","ext_blunt_high_high_11.wav","ext_blunt_high_high_12.wav","ext_blunt_high_high_13.wav","ext_blunt_high_high_14.wav","ext_blunt_high_high_15.wav","ext_blunt_high_high_16.wav"]),
# ("wooden_hit_high_armor_high_damage",	sf_priority_5|sf_vol_9,										["min_blunt_high_high_01.wav","min_blunt_high_high_02.wav","min_blunt_high_high_03.wav"]),
 ("mp_arrow_hit_target",				sf_2d|sf_priority_10|sf_vol_9,								["min_mp_arrow_hit_target.wav"]),
 ("blunt_hit",							sf_priority_5|sf_vol_10,									["min_blunt_hit_01.wav","min_blunt_hit_02.wav","min_blunt_hit_03.wav","ext_blunt_hit_04.wav","ext_blunt_hit_05.wav","ext_blunt_hit_06.wav","ext_blunt_hit_07.wav","ext_blunt_hit_08.wav","ext_blunt_hit_09.wav","ext_blunt_hit_10.wav","ext_blunt_hit_11.wav","ext_blunt_hit_12.wav","ext_blunt_hit_13.wav","ext_blunt_hit_14.wav","ext_blunt_hit_15.wav","ext_blunt_hit_16.wav"]),
# ("blunt_hit",							sf_priority_5|sf_vol_10,									["min_blunt_hit_01.wav","min_blunt_hit_02.wav","min_blunt_hit_03.wav"]),
 ("player_hit_by_arrow",				sf_priority_10|sf_vol_10,									["min_player_hit_by_arrow.wav"]),

#Pistol shot
 ("pistol_shot",						sf_priority_10|sf_vol_10,									["min_gun_shoot_01.wav","ext_gun_shoot_02.wav","ext_gun_shoot_03.wav","ext_gun_shoot_04.wav","ext_gun_shoot_05.wav","ext_gun_shoot_06.wav","ext_gun_shoot_07.wav","ext_gun_shoot_08.wav","ext_gun_shoot_09.wav","ext_gun_shoot_10.wav","ext_gun_shoot_11.wav"]),
# ("pistol_shot",						sf_priority_10|sf_vol_10,									["min_gun_shoot_01.wav"]),

#Male shouts and such
 ("man_grunt",							sf_priority_3|sf_vol_4,										["min_man_heavy_grunt_01.wav","min_man_heavy_grunt_02.wav","min_man_heavy_grunt_03.wav","ext_man_heavy_grunt_04.wav","ext_man_heavy_grunt_05.wav","ext_man_heavy_grunt_06.wav","ext_man_heavy_grunt_07.wav","ext_man_heavy_grunt_08.wav","ext_man_heavy_grunt_09.wav","ext_man_heavy_grunt_10.wav","ext_man_heavy_grunt_11.wav","ext_man_heavy_grunt_12.wav","ext_man_heavy_grunt_13.wav","ext_man_heavy_grunt_14.wav","ext_man_heavy_grunt_15.wav","ext_man_heavy_grunt_16.wav","ext_man_heavy_grunt_17.wav","ext_man_heavy_grunt_18.wav"]),
# ("man_grunt",							sf_priority_3|sf_vol_4,										["min_man_heavy_grunt_01.wav","min_man_heavy_grunt_02.wav","min_man_heavy_grunt_03.wav"]),
 ("man_breath_hard",					sf_priority_3|sf_vol_8,										["min_man_ugh_01.wav","min_man_ugh_02.wav","min_man_ugh_03.wav","min_man_ugh_04.wav","min_man_ugh_05.wav","min_man_ugh_06.wav","min_man_ugh_07.wav"]),
 ("man_stun",							sf_priority_3|sf_vol_9,										["min_man_short_grunt_01.wav","ext_man_short_grunt_02.wav","ext_man_short_grunt_03.wav","ext_man_short_grunt_04.wav"]),
# ("man_stun",							sf_priority_3|sf_vol_9,										["min_man_short_grunt_01.wav"]),
 ("man_grunt_long",						sf_priority_3|sf_vol_8,										["min_man_heavy_grunt_long_01.wav","min_man_heavy_grunt_long_02.wav","min_man_heavy_grunt_long_03.wav","min_man_heavy_grunt_long_04.wav","min_man_heavy_grunt_long_05.wav","min_man_heavy_grunt_long_06.wav","ext_man_heavy_grunt_long_07.wav","ext_man_heavy_grunt_long_08.wav","ext_man_heavy_grunt_long_09.wav","ext_man_heavy_grunt_long_10.wav","ext_man_heavy_grunt_long_11.wav","ext_man_heavy_grunt_long_12.wav","ext_man_heavy_grunt_long_13.wav","ext_man_heavy_grunt_long_14.wav","ext_man_heavy_grunt_long_15.wav"]),
 ("man_yell",							sf_priority_3|sf_vol_7,										["min_man_yell_01.wav","min_man_yell_02.wav","min_man_yell_03.wav","min_man_yell_04.wav","min_man_yell_05.wav","min_man_yell_06.wav","min_man_yell_07.wav","min_man_yell_08.wav","min_man_yell_09.wav","min_man_yell_10.wav","min_man_yell_11.wav","min_man_yell_12.wav","min_man_yell_13.wav","min_man_yell_14.wav","min_man_yell_15.wav","min_man_yell_16.wav","min_man_yell_17.wav","min_man_yell_18.wav","min_man_yell_19.wav","ext_man_yell_20.wav","ext_man_yell_21.wav","ext_man_yell_22.wav","ext_man_yell_23.wav","ext_man_yell_24.wav","ext_man_yell_25.wav","ext_man_yell_26.wav","ext_man_yell_27.wav","ext_man_yell_28.wav","ext_man_yell_29.wav","ext_man_yell_30.wav","ext_man_yell_31.wav","ext_man_yell_32.wav"]),
# ("man_yell",							sf_priority_3|sf_vol_7,										["min_man_yell_01.wav","min_man_yell_02.wav","min_man_yell_03.wav","min_man_yell_04.wav","min_man_yell_05.wav","min_man_yell_06.wav","min_man_yell_07.wav","min_man_yell_08.wav","min_man_yell_09.wav","min_man_yell_10.wav","min_man_yell_11.wav","min_man_yell_12.wav","min_man_yell_13.wav","min_man_yell_14.wav","min_man_yell_15.wav","min_man_yell_16.wav","min_man_yell_17.wav","min_man_yell_18.wav","min_man_yell_19.wav"]),
 ("man_warcry",							sf_priority_6,												["min_man_insult_01.wav","min_man_insult_02.wav","min_man_insult_03.wav","min_man_insult_04.wav","min_man_insult_05.wav","min_man_insult_06.wav","min_man_insult_07.wav","ext_man_insult_08.wav","ext_man_insult_09.wav","ext_man_insult_10.wav","ext_man_insult_11.wav","ext_man_insult_12.wav","ext_man_insult_13.wav","ext_man_insult_14.wav","ext_man_insult_15.wav","ext_man_insult_16.wav","ext_man_insult_17.wav","ext_man_insult_18.wav","ext_man_insult_19.wav","ext_man_insult_20.wav","ext_man_insult_21.wav","ext_man_insult_22.wav","ext_man_insult_23.wav","ext_man_insult_24.wav","ext_man_insult_25.wav"]),
# ("man_warcry",						sf_priority_6,												["min_man_insult_01.wav","min_man_insult_02.wav","min_man_insult_03.wav","min_man_insult_04.wav","min_man_insult_05.wav","min_man_insult_06.wav","min_man_insult_07.wav"]),

#Encounters
 ("encounter_looters",					sf_2d|sf_vol_8,												["min_encounter_river_pirates_01.wav","min_encounter_river_pirates_02.wav","min_encounter_river_pirates_03.wav","min_encounter_river_pirates_04.wav","min_encounter_river_pirates_05.wav","ext_encounter_river_pirates_06.wav","ext_encounter_river_pirates_07.wav"]),
# ("encounter_looters",					sf_2d|sf_vol_8,												["min_encounter_river_pirates_01.wav","min_encounter_river_pirates_02.wav","min_encounter_river_pirates_03.wav","min_encounter_river_pirates_04.wav","min_encounter_river_pirates_05.wav"]),
 ("encounter_bandits",					sf_2d|sf_vol_8,												["min_encounter_bandit_01.wav","min_encounter_bandit_02.wav","min_encounter_bandit_03.wav","min_encounter_bandit_04.wav","min_encounter_bandit_05.wav","min_encounter_bandit_06.wav","min_encounter_bandit_07.wav",]),
 ("encounter_farmers",					sf_2d|sf_vol_8,												["min_encounter_farmer_01.wav","min_encounter_farmer_02.wav","min_encounter_farmer_03.wav","min_encounter_farmer_04.wav","ext_encounter_farmer_05.wav","ext_encounter_farmer_06.wav"]),
# ("encounter_farmers",					sf_2d|sf_vol_8,												["min_encounter_farmer_01.wav","min_encounter_farmer_02.wav","min_encounter_farmer_03.wav","min_encounter_farmer_04.wav"]),
 ("encounter_sea_raiders",				sf_2d|sf_vol_8,												["min_encounter_sea_raider_01.wav","min_encounter_sea_raider_02.wav","min_encounter_sea_raider_03.wav","min_encounter_sea_raider_04.wav","ext_encounter_sea_raider_05.wav","ext_encounter_sea_raider_06.wav"]),
# ("encounter_sea_raiders",				sf_2d|sf_vol_8,												["min_encounter_sea_raider_01.wav","min_encounter_sea_raider_02.wav","min_encounter_sea_raider_03.wav","min_encounter_sea_raider_04.wav"]),
 ("encounter_steppe_bandits",			sf_2d|sf_vol_8,												["min_encounter_steppe_bandit_01.wav","min_encounter_steppe_bandit_02.wav","min_encounter_steppe_bandit_03.wav","min_encounter_steppe_bandit_04.wav","min_encounter_steppe_bandit_05.wav","ext_encounter_steppe_bandit_06.wav","ext_encounter_steppe_bandit_07.wav","ext_encounter_steppe_bandit_08.wav"]),
# ("encounter_steppe_bandits",			sf_2d|sf_vol_8,												["min_encounter_steppe_bandit_01.wav","min_encounter_steppe_bandit_02.wav","min_encounter_steppe_bandit_03.wav","min_encounter_steppe_bandit_04.wav","min_encounter_steppe_bandit_05.wav"]),
 ("encounter_nobleman",					sf_2d|sf_vol_8,												["min_encounter_nobleman_01.wav"]),
 ("encounter_vaegirs_ally",				sf_2d|sf_vol_8,												["min_encounter_vaegirs_ally_01.wav","min_encounter_vaegirs_ally_02.wav","ext_encounter_vaegirs_ally_03.wav","ext_encounter_vaegirs_ally_04.wav"]),
# ("encounter_vaegirs_ally",			sf_2d|sf_vol_8,												["min_encounter_vaegirs_ally_01.wav","min_encounter_vaegirs_ally_02.wav"]),
 ("encounter_vaegirs_neutral",			sf_2d|sf_vol_8,												["min_encounter_vaegirs_neutral_01.wav","min_encounter_vaegirs_neutral_04.wav","min_encounter_vaegirs_neutral_06.wav","min_encounter_vaegirs_neutral_08.wav"]),
 ("encounter_vaegirs_enemy",			sf_2d|sf_vol_8,												["min_encounter_vaegirs_neutral_02.wav","min_encounter_vaegirs_neutral_03.wav","min_encounter_vaegirs_neutral_05.wav","min_encounter_vaegirs_neutral_07.wav"]),
 ("sneak_town_halt",					sf_2d,														["min_sneak_halt_01.wav","min_sneak_halt_02.wav"]),

#Horse moving
 ("horse_walk",							sf_priority_3|sf_vol_10,									["min_horse_walk_01.wav","min_horse_walk_02.wav","min_horse_walk_03.wav","min_horse_walk_04.wav","ext_horse_walk_05.wav","ext_horse_walk_06.wav","ext_horse_walk_07.wav","ext_horse_walk_08.wav","ext_horse_walk_09.wav","ext_horse_walk_10.wav","ext_horse_walk_11.wav","ext_horse_walk_12.wav"]),
# ("horse_walk",						sf_priority_3|sf_vol_10,									["min_horse_walk_01.wav","min_horse_walk_02.wav","min_horse_walk_03.wav","min_horse_walk_04.wav"]),
 ("horse_trot",							sf_priority_3|sf_vol_10,									["min_horse_trot_01.wav","min_horse_trot_02.wav","min_horse_trot_03.wav","min_horse_trot_04.wav","ext_horse_trot_05.wav","ext_horse_trot_06.wav","ext_horse_trot_07.wav","ext_horse_trot_08.wav","ext_horse_trot_09.wav","ext_horse_trot_10.wav","ext_horse_trot_11.wav","ext_horse_trot_12.wav"]),
# ("horse_trot",						sf_priority_3|sf_vol_10,									["min_horse_trot_01.wav","min_horse_trot_02.wav","min_horse_trot_03.wav","min_horse_trot_04.wav"]),
 ("horse_canter",						sf_priority_3|sf_vol_13,									["min_horse_canter_01.wav","min_horse_canter_02.wav","min_horse_canter_03.wav","min_horse_canter_04.wav","ext_horse_canter_05.wav","ext_horse_canter_06.wav","ext_horse_canter_07.wav","ext_horse_canter_08.wav","ext_horse_canter_09.wav","ext_horse_canter_10.wav","ext_horse_canter_11.wav","ext_horse_canter_12.wav"]),
# ("horse_canter",						sf_priority_3|sf_vol_13,									["min_horse_canter_01.wav","min_horse_canter_02.wav","min_horse_canter_03.wav","min_horse_canter_04.wav"]),
 ("horse_gallop",						sf_priority_3|sf_vol_13,									["min_horse_gallop_01.wav","min_horse_gallop_02.wav","min_horse_gallop_03.wav","min_horse_gallop_04.wav","ext_horse_gallop_05.wav","ext_horse_gallop_06.wav","ext_horse_gallop_07.wav","ext_horse_gallop_08.wav","ext_horse_gallop_09.wav","ext_horse_gallop_10.wav","ext_horse_gallop_11.wav","ext_horse_gallop_12.wav"]),
# ("horse_gallop",						sf_priority_3|sf_vol_13,									["min_horse_gallop_01.wav","min_horse_gallop_02.wav","min_horse_gallop_03.wav","min_horse_gallop_04.wav"]),

#Other horse sounds
 ("horse_breath",						sf_priority_3|sf_priority_9|sf_vol_10,						["min_horse_breath_01.wav","min_horse_breath_02.wav","min_horse_breath_03.wav","min_horse_breath_04.wav"]),
 ("horse_snort",						sf_priority_5|sf_vol_10,									["min_horse_snort_01.wav","min_horse_snort_02.wav","min_horse_snort_03.wav","min_horse_snort_04.wav","min_horse_snort_05.wav","ext_horse_snort_06.wav","ext_horse_snort_07.wav","ext_horse_snort_08.wav"]),
# ("horse_snort",						sf_priority_5|sf_vol_10,									["min_horse_snort_01.wav","min_horse_snort_02.wav","min_horse_snort_03.wav","min_horse_snort_04.wav","min_horse_snort_05.wav"]),
 ("horse_low_whinny",					sf_vol_12,													["min_horse_whinny_01.wav","min_horse_whinny_02.wav"]),

#Man hit
 ("block_fist",							0,															["min_block_fist_01.wav","min_block_fist_02.wav"]),
 ("man_hit_blunt_weak",					sf_priority_5|sf_vol_10,									["min_man_hit_01.wav","min_man_hit_02.wav","min_man_hit_03.wav","min_man_hit_04.wav","min_man_hit_05.wav","ext_man_hit_06.wav","ext_man_hit_07.wav"]),
# ("man_hit_blunt_weak",				sf_priority_5|sf_vol_10,									["min_man_hit_01.wav","min_man_hit_02.wav","min_man_hit_03.wav","min_man_hit_04.wav","min_man_hit_05.wav"]),
 ("man_hit_blunt_strong",				sf_priority_5|sf_vol_10,									["min_man_hit_08.wav","min_man_hit_09.wav","min_man_hit_10.wav","min_man_hit_11.wav","min_man_hit_12.wav","ext_man_hit_13.wav","ext_man_hit_14.wav"]),
# ("man_hit_blunt_strong",				sf_priority_5|sf_vol_10,									["min_man_hit_08.wav","min_man_hit_09.wav","min_man_hit_10.wav","min_man_hit_11.wav","min_man_hit_12.wav"]),
 ("man_hit_pierce_weak",				sf_priority_5|sf_vol_10,									["min_man_hit_15.wav","min_man_hit_16.wav","min_man_hit_17.wav","min_man_hit_18.wav","min_man_hit_19.wav","ext_man_hit_20.wav","ext_man_hit_21.wav"]),
# ("man_hit_pierce_weak",				sf_priority_5|sf_vol_10,									["min_man_hit_15.wav","min_man_hit_16.wav","min_man_hit_17.wav","min_man_hit_18.wav","min_man_hit_19.wav"]),
 ("man_hit_pierce_strong",				sf_priority_5|sf_vol_10,									["min_man_hit_22.wav","min_man_hit_23.wav","min_man_hit_24.wav","min_man_hit_25.wav","min_man_hit_26.wav","ext_man_hit_27.wav","ext_man_hit_28.wav"]),
# ("man_hit_pierce_strong",				sf_priority_5|sf_vol_10,									["min_man_hit_22.wav","min_man_hit_23.wav","min_man_hit_24.wav","min_man_hit_25.wav","min_man_hit_26.wav"]),
 ("man_hit_cut_weak",					sf_priority_5|sf_vol_10,									["min_man_hit_29.wav","min_man_hit_30.wav","min_man_hit_31.wav","min_man_hit_32.wav","min_man_hit_33.wav","ext_man_hit_34.wav","ext_man_hit_35.wav"]),
# ("man_hit_cut_weak",					sf_priority_5|sf_vol_10,									["min_man_hit_29.wav","min_man_hit_30.wav","min_man_hit_31.wav","min_man_hit_32.wav","min_man_hit_33.wav"]),
 ("man_hit_cut_strong",					sf_priority_5|sf_vol_10,									["min_man_hit_36.wav","min_man_hit_37.wav","min_man_hit_38.wav","min_man_hit_39.wav","min_man_hit_40.wav","ext_man_hit_41.wav","ext_man_hit_42.wav"]),
# ("man_hit_cut_strong",				sf_priority_5|sf_vol_10,									["min_man_hit_36.wav","min_man_hit_37.wav","min_man_hit_38.wav","min_man_hit_39.wav","min_man_hit_40.wav"]),

#Man victory
 ("man_victory",						sf_priority_5|sf_vol_9,										["min_man_victory_01.wav","min_man_victory_02.wav","min_man_victory_03.wav","min_man_victory_04.wav","min_man_victory_05.wav","min_man_victory_06.wav","min_man_victory_07.wav","min_man_victory_08.wav","min_man_victory_09.wav","min_man_victory_10.wav","ext_man_victory_11.wav","ext_man_victory_12.wav","ext_man_victory_13.wav","ext_man_victory_14.wav","ext_man_victory_15.wav","ext_man_victory_16.wav","ext_man_victory_17.wav","ext_man_victory_18.wav","ext_man_victory_19.wav","ext_man_victory_20.wav"]),
# ("man_victory",						sf_priority_5|sf_vol_9,										["min_man_victory_01.wav","min_man_victory_02.wav","min_man_victory_03.wav","min_man_victory_04.wav","min_man_victory_05.wav","min_man_victory_06.wav","min_man_victory_07.wav","min_man_victory_08.wav","min_man_victory_09.wav","min_man_victory_10.wav"]),

#More General Sounds
 ("fire_loop",							sf_priority_9|sf_vol_4|sf_looping|sf_start_at_random_pos,	["min_Fire_Small_Crackle_Slick_op.wav"]),
 ("torch_loop",							sf_priority_9|sf_vol_4|sf_looping|sf_start_at_random_pos,	["min_Fire_Torch_Loop3.wav","ext_Fire_Torch_Loop3_new.wav"]),
# ("torch_loop",						sf_priority_9|sf_vol_4|sf_looping|sf_start_at_random_pos,	["min_Fire_Torch_Loop3.wav"]),
 ("dummy_hit",							sf_priority_9,												["min_dummy_hit_01.wav","min_dummy_hit_02.wav","ext_dummy_hit_03.wav"]),
# ("dummy_hit",							sf_priority_9,												["min_dummy_hit_01.wav","min_dummy_hit_02.wav"]),
 ("dummy_destroyed",					sf_priority_9,												["min_dummy_break_01.wav","ext_dummy_break_02.wav","ext_dummy_break_03.wav","ext_dummy_break_04.wav","ext_dummy_break_05.wav"]),
# ("dummy_destroyed",					sf_priority_9,												["min_dummy_break_01.wav"]),
 ("gourd_destroyed",					sf_priority_9,												["min_dummy_break_01.wav","ext_dummy_break_02.wav","ext_dummy_break_03.wav","ext_dummy_break_04.wav","ext_dummy_break_05.wav"]),
# ("gourd_destroyed",					sf_priority_9,												["min_dummy_break_01.wav"]),
 ("cow_moo",							sf_2d|sf_priority_9|sf_vol_8,								["min_cow_moo_1.wav"]),
 ("cow_slaughter",						sf_2d|sf_priority_9|sf_vol_8,								["min_cow_slaughter_01.wav","ext_cow_slaughter_02.wav"]),
# ("cow_slaughter",						sf_2d|sf_priority_9|sf_vol_8,								["min_cow_slaughter_01.wav"]),
 ("distant_dog_bark",					sf_2d|sf_priority_8|sf_vol_8,								["min_d_dog1.wav","min_d_dog2.wav","min_d_dog3.wav","min_d_dog4.wav"]),
 ("distant_owl",						sf_2d|sf_priority_8|sf_vol_9,								["min_d_owl1.wav","min_d_owl2.wav","min_d_owl3.wav"]),
 ("distant_chicken",					sf_2d|sf_priority_8|sf_vol_8,								["min_d_chicken1.wav","min_d_chicken2.wav"]),
 ("distant_carpenter",					sf_2d|sf_priority_8|sf_vol_3,								["min_d_carpenter1.wav","min_d_saw_short3.wav"]),
 ("distant_blacksmith",					sf_2d|sf_priority_8|sf_vol_4,								["min_d_blacksmith2.wav"]),
 ("arena_ambiance",						sf_2d|sf_priority_8|sf_vol_3|sf_looping,					["min_arena_loop1.wav","ext_arena_loop2.wav","ext_arena_loop3.wav","ext_arena_loop4.wav"]),
# ("arena_ambiance",					sf_2d|sf_priority_8|sf_vol_3|sf_looping,					["min_arena_loop1.wav"]),
 ("town_ambiance",						sf_2d|sf_priority_8|sf_vol_3|sf_looping,					["min_town_loop_3.wav"]),
 ("tutorial_fail",						sf_2d|sf_vol_7,												["min_cue_failure.wav"]),
 ("your_flag_taken",					sf_2d|sf_priority_10|sf_vol_10,								["min_your_flag_taken.wav"]),
 ("enemy_flag_taken",					sf_2d|sf_priority_10|sf_vol_10,								["min_enemy_flag_taken.wav"]),
 ("flag_returned",						sf_2d|sf_priority_10|sf_vol_10,								["min_your_flag_returned.wav"]),
 ("team_scored_a_point",				sf_2d|sf_priority_10|sf_vol_10,								["min_you_scored_a_point.wav"]),
 ("enemy_scored_a_point",				sf_2d|sf_priority_10|sf_vol_10,								["min_enemy_scored_a_point.wav"]),
 ("whistle",							sf_priority_9,												["min_whistle.wav"]), #Floris
]
# modmerger_start version=201 type=2
try:
    component_name = "sounds"
    var_set = { "sounds" : sounds }
    from modmerger import modmerge
    modmerge(var_set)
except:
    raise
# modmerger_end
