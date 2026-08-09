# test_robot.py — testing classes

from robot import Camera, Motor
import pytest


class TestCamera:
    """Tests for the Camera class."""

    def test_default_resolution(self):
        """Camera should default to 1920x1080."""
        cam = Camera()
        assert cam.resolution == (1920, 1080)

    def test_custom_resolution(self):
        """Camera should accept custom resolution."""
        cam = Camera((1280, 720))
        assert cam.resolution == (1280, 720)

    def test_read(self):
        """Read should return a string with resolution."""
        cam = Camera()
        result = cam.read()
        assert "1920" in result
        assert "1080" in result


class TestMotor:
    """Tests for the Motor class."""

    @pytest.fixture
    def motor(self):
        """Create a fresh Motor for each test."""
        return Motor(max_speed=100)

    def test_initial_speed(self, motor):
        """Motor should start at speed 0."""
        assert motor.current_speed == 0

    def test_set_speed(self, motor):
        """Motor should set speed correctly."""
        result = motor.set_speed(50)
        assert result == 50
        assert motor.current_speed == 50

    def test_max_speed_limit(self, motor):
        """Motor should not exceed max speed."""
        result = motor.set_speed(200)
        assert result == 100  # capped at max_speed
        assert motor.current_speed == 100