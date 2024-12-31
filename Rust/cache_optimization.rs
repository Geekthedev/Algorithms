use std::collections::HashMap;

struct LRUCache<K, V> {
    capacity: usize,
    map: HashMap<K, V>,
    keys: Vec<K>,
}

impl<K: Eq + std::hash::Hash + Clone, V> LRUCache<K, V> {
    // Initialize a new LRU Cache with the given capacity
    fn new(capacity: usize) -> Self {
        LRUCache {
            capacity,
            map: HashMap::new(),
            keys: Vec::new(),
        }
    }

    // Get a value from the cache
    fn get(&mut self, key: &K) -> Option<&V> {
        if let Some(index) = self.keys.iter().position(|k| k == key) {
            let key = self.keys.remove(index);
            self.keys.push(key.clone());
        }
        self.map.get(key)
    }

    // Insert a key-value pair into the cache
    fn put(&mut self, key: K, value: V) {
        if self.map.contains_key(&key) {
            self.map.insert(key.clone(), value);
            self.keys.retain(|k| k != &key);
            self.keys.push(key);
        } else {
            if self.keys.len() == self.capacity {
                if let Some(removed_key) = self.keys.remove(0) {
                    self.map.remove(&removed_key);
                }
            }
            self.keys.push(key.clone());
            self.map.insert(key, value);
        }
    }
}

fn main() {
    let mut cache = LRUCache::new(3);

    // Add items to the cache
    cache.put("A", 1);
    cache.put("B", 2);
    cache.put("C", 3);

    println!("{:?}", cache.get(&"A")); // Some(1)
    println!("{:?}", cache.get(&"B")); // Some(2)

    // Add a new item, causing the least recently used ("C") to be evicted
    cache.put("D", 4);

    println!("{:?}", cache.get(&"C")); // None
    println!("{:?}", cache.get(&"D")); // Some(4)
}
