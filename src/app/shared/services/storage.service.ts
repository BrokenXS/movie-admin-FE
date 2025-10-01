import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class LocalStorageService {
  private isLocalStorageAvailable(): boolean {
    return typeof window !== 'undefined' && typeof window.localStorage !== 'undefined';
  }

  get(key: string) {
    if (this.isLocalStorageAvailable()) {
      return JSON.parse(localStorage.getItem(key) || '{}') || {};
    }
    return {};
  }

  set(key: string, value: any): boolean {
    if (this.isLocalStorageAvailable()) {
      localStorage.setItem(key, JSON.stringify(value));
      return true;
    }
    return false;
  }

  has(key: string): boolean {
    if (this.isLocalStorageAvailable()) {
      return !!localStorage.getItem(key);
    }
    return false;
  }

  remove(key: string) {
    if (this.isLocalStorageAvailable()) {
      localStorage.removeItem(key);
    }
  }

  clear() {
    if (this.isLocalStorageAvailable()) {
      localStorage.clear();
    }
  }
}

export class MemoryStorageService {
  private store: Record<string, string> = {};

  get(key: string) {
    return JSON.parse(this.store[key] || '{}') || {};
  }

  set(key: string, value: any): boolean {
    this.store[key] = JSON.stringify(value);
    return true;
  }

  has(key: string): boolean {
    return !!this.store[key];
  }

  remove(key: string) {
    delete this.store[key];
  }

  clear() {
    this.store = {};
  }
}
