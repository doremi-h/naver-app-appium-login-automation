# NAVER Mobile Automation Test

Appium을 학습하면서 Android 실기기 환경에서 네이버 앱의 로그인 후 메일 화면까지 이동하는 자동화 흐름을 직접 구현해본 프로젝트입니다.

QA 업무에서 자동화에 대한 이해도를 높이기 위해  
Appium 환경 구축부터 UI 요소 탐색, 로그인 시나리오 구현까지 직접 테스트하며 학습한 기록을 정리했습니다.


## Test Scenario

1. Launch NAVER app
2. Open menu
3. Navigate to login
4. Input ID and password
5. Login
6. Close popup
7. Open Mail
8. Verify mail screen


## Tech Stack

- Python
- Appium
- UiAutomator2
- Android Real Device


# NAVER Mobile Login Automation Test

Appium 기반으로 Android 환경에서 NAVER 모바일 앱 로그인 시나리오를 자동화 테스트로 구현한 프로젝트입니다.

QA 엔지니어로서 모바일 서비스의 주요 사용자 흐름(User Flow)을 자동화 테스트로 검증하는 과정을 학습하기 위해 진행했습니다.
실제 서비스 QA 경험에서 자주 검증하게 되는 로그인 → 메일 화면 진입 흐름을 기준으로 테스트 시나리오를 설계하고 자동화했습니다.


# Project Purpose

모바일 서비스 QA 업무에서는 다음과 같은 상황이 자주 발생합니다.

- 릴리즈 전 반복적인 로그인 검증

- 사용자 핵심 흐름(로그인, 메인 진입 등) 기능 점검

- 주요 기능 Regression 테스트

이 프로젝트는 이러한 반복 검증을 자동화하여 핵심 사용자 흐름을 안정적으로 검증하는 테스트 자동화 기반을 이해하는 것을 목표로 합니다.


# Test Scenario

NAVER 앱에서 로그인 후 메일 화면으로 이동하는 기본 사용자 흐름을 자동화했습니다.

1. NAVER 앱 실행

2. 메뉴 진입

3. 로그인 화면 이동

4. ID / Password 입력

5. 로그인 수행

6. 메일 화면 이동

7. 메일 화면 정상 진입 여부 확인


# Test Flow
App Launch

   ↓

Open Menu

   ↓
   
Navigate Login

   ↓
   
Input ID / Password

   ↓
   
Login

   ↓
   
Close Popup

   ↓
   
Open Mail

   ↓
   
Verify Mail Screen


# Tech Stack

- Python

- Appium

- UiAutomator2

- Android Device


# Test Environment

- macOS

- Android Device

- Appium Server

- Python 3.9.6


# What I Learned

이 프로젝트를 통해 다음과 같은 자동화 테스트 경험을 쌓았습니다.

- Appium 환경 구축 및 Android 디바이스 연결

- 모바일 UI Element 탐색 및 제어

- 사용자 로그인 시나리오 자동화 구현

- 모바일 사용자 흐름 기반 테스트 설계 경험


# About Me

모바일 서비스 QA 엔지니어로서
사용자 경험(User Experience) 기반의 테스트 설계와 서비스 품질 개선에 관심이 있습니다.

본 프로젝트는 QA 업무에서 반복되는 사용자 핵심 흐름을 자동화 테스트로 구현해보며
모바일 테스트 자동화 역량을 확장하기 위해 진행했습니다.


# Author

QA Engineer
GitHub: https://github.com/doremi-h
