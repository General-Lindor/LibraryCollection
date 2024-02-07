package de.kalender.utils;
import java.util.HashMap;

public class DualMap {

	private HashMap map = new HashMap();

	public boolean put(Object objA, Object objB) {
		if ((map.get(objA) != null) | (map.get(objB) != null)) {
			return false;
		}
		map.put(objA, objB);
		map.put(objB, objA);
		return true;
	}

	public Object get(Object key) {
		return map.get(key);
	}

	public void remove(Object key) {
		Object other = map.get(key);
		map.remove(key);
		map.remove(other);
	}
}
