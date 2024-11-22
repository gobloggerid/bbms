# Released under the MIT License. See LICENSE for details.
#
"""Common shared Ballistica components.

For modding purposes, this package should generally not be used directly.
Instead one should use purpose-built packages such as bascenev1 or bauiv1
which themselves import various functionality from here and reexpose it in
a more focused way.
"""
# pylint: disable=redefined-builtin

# The stuff we expose here at the top level is our 'public' api for use
# from other modules/packages. Code *within* this package should import
# things from this package's submodules directly to reduce the chance of
# dependency loops. The exception is TYPE_CHECKING blocks and
# annotations since those aren't evaluated at runtime.

from efro.util import set_canonical_module_names


import _babase
from _babase import (
    add_clean_frame_callback,
    android_get_external_files_dir,
    appname,
    appnameupper,
    apptime,
    apptimer,
    AppTimer,
    fullscreen_control_available,
    fullscreen_control_get,
    fullscreen_control_key_shortcut,
    fullscreen_control_set,
    charstr,
    clipboard_get_text,
    clipboard_has_text,
    clipboard_is_supported,
    clipboard_set_text,
    ContextCall,
    ContextRef,
    displaytime,
    displaytimer,
    DisplayTimer,
    do_once,
    env,
    Env,
    fade_screen,
    fatal_error,
    get_display_resolution,
    get_immediate_return_code,
    get_input_idle_time,
    get_low_level_config_value,
    get_max_graphics_quality,
    get_replays_dir,
    get_string_height,
    get_string_width,
    get_v1_cloud_log_file_path,
    getsimplesound,
    has_user_run_commands,
    have_chars,
    have_permission,
    in_logic_thread,
    increment_analytics_count,
    invoke_main_menu,
    is_os_playing_music,
    is_xcode_build,
    lock_all_input,
    mac_music_app_get_playlists,
    mac_music_app_get_volume,
    mac_music_app_init,
    mac_music_app_play_playlist,
    mac_music_app_set_volume,
    mac_music_app_stop,
    music_player_play,
    music_player_set_volume,
    music_player_shutdown,
    music_player_stop,
    native_review_request,
    native_review_request_supported,
    native_stack_trace,
    open_file_externally,
    open_url,
    overlay_web_browser_close,
    overlay_web_browser_is_open,
    overlay_web_browser_is_supported,
    overlay_web_browser_open_url,
    print_load_info,
    pushcall,
    quit,
    reload_media,
    request_permission,
    safecolor,
    screenmessage,
    set_analytics_screen,
    set_low_level_config_value,
    set_thread_name,
    set_ui_input_device,
    show_progress_bar,
    shutdown_suppress_begin,
    shutdown_suppress_end,
    shutdown_suppress_count,
    SimpleSound,
    supports_max_fps,
    supports_vsync,
    unlock_all_input,
    user_agent_string,
    Vec3,
    workspaces_in_use,
)

from babase._accountv2 import AccountV2Handle, AccountV2Subsystem
from babase._app import App
from babase._appconfig import commit_app_config
from babase._appintent import AppIntent, AppIntentDefault, AppIntentExec
from babase._appmode import AppMode
from babase._appsubsystem import AppSubsystem
from babase._appmodeselector import AppModeSelector
from babase._appconfig import AppConfig
from babase._apputils import (
    handle_leftover_v1_cloud_log_file,
    is_browser_likely_available,
    garbage_collect,
    get_remote_app_name,
    AppHealthMonitor,
)
from babase._devconsole import (
    DevConsoleTab,
    DevConsoleTabEntry,
    DevConsoleSubsystem,
)
from babase._emptyappmode import EmptyAppMode
from babase._error import (
    print_exception,
    print_error,
    ContextError,
    NotFoundError,
    PlayerNotFoundError,
    SessionPlayerNotFoundError,
    NodeNotFoundError,
    ActorNotFoundError,
    InputDeviceNotFoundError,
    WidgetNotFoundError,
    ActivityNotFoundError,
    TeamNotFoundError,
    MapNotFoundError,
    SessionTeamNotFoundError,
    SessionNotFoundError,
    DelegateNotFoundError,
)
from babase._general import (
    utf8_all,
    DisplayTime,
    AppTime,
    WeakCall,
    Call,
    existing,
    Existable,
    verify_object_death,
    storagename,
    getclass,
    get_type_name,
)
from babase._language import Lstr, LanguageSubsystem
from babase._login import LoginAdapter, LoginInfo

# noinspection PyProtectedMember
# (PyCharm inspection bug?)
from babase._mgen.enums import (
    Permission,
    SpecialChar,
    InputType,
    UIScale,
    QuitType,
)
from babase._math import normalized_color, is_point_in_box, vec3validate
from babase._meta import MetadataSubsystem
from babase._net import get_ip_address_type, DEFAULT_REQUEST_TIMEOUT_SECONDS
from babase._plugin import PluginSpec, Plugin, PluginSubsystem
from babase._stringedit import StringEditAdapter, StringEditSubsystem
from babase._text import timestring

_babase.app = app = App()
app.postinit()

__all__ = [
    'AccountV2Handle',
    'AccountV2Subsystem',
    'ActivityNotFoundError',
    'ActorNotFoundError',
    'add_clean_frame_callback',
    'android_get_external_files_dir',
    'app',
    'app',
    'App',
    'AppConfig',
    'AppHealthMonitor',
    'AppIntent',
    'AppIntentDefault',
    'AppIntentExec',
    'AppMode',
    'appname',
    'appnameupper',
    'AppModeSelector',
    'AppSubsystem',
    'apptime',
    'AppTime',
    'apptime',
    'apptimer',
    'AppTimer',
    'Call',
    'fullscreen_control_available',
    'fullscreen_control_get',
    'fullscreen_control_key_shortcut',
    'fullscreen_control_set',
    'charstr',
    'clipboard_get_text',
    'clipboard_has_text',
    'clipboard_is_supported',
    'clipboard_set_text',
    'commit_app_config',
    'ContextCall',
    'ContextError',
    'ContextRef',
    'DelegateNotFoundError',
    'DevConsoleTab',
    'DevConsoleTabEntry',
    'DevConsoleSubsystem',
    'DisplayTime',
    'displaytime',
    'displaytimer',
    'DisplayTimer',
    'do_once',
    'EmptyAppMode',
    'env',
    'Env',
    'Existable',
    'existing',
    'fade_screen',
    'fatal_error',
    'garbage_collect',
    'get_display_resolution',
    'get_immediate_return_code',
    'get_input_idle_time',
    'get_ip_address_type',
    'get_low_level_config_value',
    'get_max_graphics_quality',
    'get_remote_app_name',
    'get_replays_dir',
    'get_string_height',
    'get_string_width',
    'get_v1_cloud_log_file_path',
    'get_type_name',
    'getclass',
    'getsimplesound',
    'handle_leftover_v1_cloud_log_file',
    'has_user_run_commands',
    'have_chars',
    'have_permission',
    'in_logic_thread',
    'increment_analytics_count',
    'InputDeviceNotFoundError',
    'InputType',
    'invoke_main_menu',
    'is_browser_likely_available',
    'is_browser_likely_available',
    'is_os_playing_music',
    'is_point_in_box',
    'is_xcode_build',
    'LanguageSubsystem',
    'lock_all_input',
    'LoginAdapter',
    'LoginInfo',
    'Lstr',
    'mac_music_app_get_playlists',
    'mac_music_app_get_volume',
    'mac_music_app_init',
    'mac_music_app_play_playlist',
    'mac_music_app_set_volume',
    'mac_music_app_stop',
    'MapNotFoundError',
    'MetadataSubsystem',
    'music_player_play',
    'music_player_set_volume',
    'music_player_shutdown',
    'music_player_stop',
    'native_review_request',
    'native_review_request_supported',
    'native_stack_trace',
    'NodeNotFoundError',
    'normalized_color',
    'NotFoundError',
    'open_file_externally',
    'open_url',
    'overlay_web_browser_close',
    'overlay_web_browser_is_open',
    'overlay_web_browser_is_supported',
    'overlay_web_browser_open_url',
    'Permission',
    'PlayerNotFoundError',
    'Plugin',
    'PluginSubsystem',
    'PluginSpec',
    'print_error',
    'print_exception',
    'print_load_info',
    'pushcall',
    'quit',
    'QuitType',
    'reload_media',
    'request_permission',
    'safecolor',
    'screenmessage',
    'SessionNotFoundError',
    'SessionPlayerNotFoundError',
    'SessionTeamNotFoundError',
    'set_analytics_screen',
    'set_low_level_config_value',
    'set_thread_name',
    'set_ui_input_device',
    'show_progress_bar',
    'shutdown_suppress_begin',
    'shutdown_suppress_end',
    'shutdown_suppress_count',
    'SimpleSound',
    'SpecialChar',
    'storagename',
    'StringEditAdapter',
    'StringEditSubsystem',
    'supports_max_fps',
    'supports_vsync',
    'TeamNotFoundError',
    'timestring',
    'UIScale',
    'unlock_all_input',
    'user_agent_string',
    'utf8_all',
    'Vec3',
    'vec3validate',
    'verify_object_death',
    'WeakCall',
    'WidgetNotFoundError',
    'workspaces_in_use',
    'DEFAULT_REQUEST_TIMEOUT_SECONDS',
]

# We want stuff to show up as babase.Foo instead of babase._sub.Foo.
set_canonical_module_names(globals())

# Allow the native layer to wrap a few things up.
_babase.reached_end_of_babase()

# Marker we pop down at the very end so other modules can run sanity
# checks to make sure we aren't importing them reciprocally when they
# import us.
_REACHED_END_OF_MODULE = True
