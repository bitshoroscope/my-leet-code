const expect = require('chai').expect;
const solution = require('../src/main.js');

describe('Tests', () => {
 it('True egg', () => {
      let result = true
      let origin = "egg"
      let expected = "add"
      expect(result).to.eql(solution.isIsomorphic(origin, expected));
      });
 it('True paper', () => {
      let result = true
      let origin = "paper"
      let expected = "title"
      expect(result).to.eql(solution.isIsomorphic(origin, expected));
      });
 it('False foo', () => {
      let result = false
      let origin = "foo"
      let expected = "bar"
      expect(result).to.eql(solution.isIsomorphic(origin, expected));
      });
 it('False badc', () => {
      let result = false
      let origin = "badc"
      let expected = "baba"
      expect(result).to.eql(solution.isIsomorphic(origin, expected));
 });
});

describe('Test iterator capabilities', () => {
      let map = new Map()
      map.set("a", "b")
      map.set("c", "d")
      map.set("e", "f")
      it('True', () => {
            expect(true).to.eql(solution.contains(map.values(), "b"));
      })
      it('False', () => {
            expect(false).to.eql(solution.contains(map.values(), "g"));
      })
})