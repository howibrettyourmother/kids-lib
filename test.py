# headless check: python3 test.py [base-url]
import asyncio,sys
from playwright.async_api import async_playwright
B=sys.argv[1] if len(sys.argv)>1 else 'http://127.0.0.1:18923/kids-lib/'
async def main():
  async with async_playwright() as p:
    b=await p.chromium.launch(executable_path='/usr/bin/google-chrome');c=await b.new_context(viewport={'width':1180,'height':820},has_touch=True,is_mobile=True)
    pg=await c.new_page();errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
    await pg.goto(B+'test.html?kid=zoe');await pg.wait_for_timeout(500);r=await pg.evaluate('window.__R');print('\n'.join(r));print('errors',errs)
    print('ALL PASS' if all(x.startswith('PASS') for x in r) and not errs else 'FAILED');await b.close()
asyncio.run(main())
