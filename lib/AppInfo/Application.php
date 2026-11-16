<?php

declare(strict_types=1);

namespace OCA\NubeTheme\AppInfo;

use OCP\AppFramework\App;
use OCP\AppFramework\Bootstrap\IBootContext;
use OCP\AppFramework\Bootstrap\IBootstrap;
use OCP\AppFramework\Bootstrap\IRegistrationContext;
use OCP\Util;

class Application extends App implements IBootstrap {
	public const APP_ID = 'nube_theme';

	public function __construct() {
		parent::__construct(self::APP_ID);
	}

	public function register(IRegistrationContext $context): void {
	}

	public function boot(IBootContext $context): void {
		// boot() runs on every request, so the styles reach logged-in, login and public pages.
		Util::addStyle(self::APP_ID, 'fonts');
		Util::addStyle(self::APP_ID, 'nube');
	}
}
