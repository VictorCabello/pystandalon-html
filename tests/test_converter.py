from cmath import exp
import os
import tempfile
import filecmp
from pystandalonehtml import converter

def test_guess_type():
    # Prepare
    basedir = os.path.dirname(__file__)
    img = '10.1.jpg'
    myPath = os.path.join(basedir, img)

    # Execute
    mime = converter.guess_type(myPath)

    # Verify
    assert('image/jpeg' == mime)


def test_file_to_base64():
    # Prepare
    basedir = os.path.dirname(__file__)
    img = '10.1.jpg'
    myPath = os.path.join(basedir, img)

    # Execute
    basestr = converter.file_to_base64(myPath)

    # Verify
    assert('/9j/4AAQSkZJRgABAQEASABIAAD//gAmRmlsZSB3cml0dGVuIGJ5IEFkb2JlIFBob3Rvc2hvcKggNS4w/9sAQwAIBgYHBgUIBwcHCQkICgwUDQwLCwwZEhMPFB0aHx4dGhwcICQuJyAiLCMcHCg3KSwwMTQ0NB8nOT04MjwuMzQy/9sAQwEJCQkMCwwYDQ0YMiEcITIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIy/8AAEQgBKgD6AwEiAAIRAQMRAf/EABwAAAICAwEBAAAAAAAAAAAAAAUGBAcAAQIDCP/EAEEQAAIBAwMCBAUCBAQEBQUBAQECAwQFEQASIQYxEyJBUQcUYXGBMpEVI0KhUmJysRYzksEkJYLR8BdDY6Lhs/H/xAAWAQEBAQAAAAAAAAAAAAAAAAAAAQL/xAAaEQEBAQEBAQEAAAAAAAAAAAAAAREhMXGB/9oADAMBAAIRAxEAPwC/tZrNa51Ub1ms1rnGg3rNazregzWa5PBJz6a2NBvWajVlfS0EfiVVTDAno0rhQf31Gpr5QVe8wVIaNBkyYIT/AKjwdAS1mosddBNCsyyDw2OATxk5x/vr1gnjnQtHKkgDEZRgRkemg9dZrliR7Y9dbydBsnAydDLLf7Z1DTzT2uqWojhlaFyoxtde40Q3BuNVH0NPF0z1rW2l4nhFVUTxTuMmJpQ26JgT2LI5XH+UaC39ZrnccdtBnvNXHUrTvapyXdlSQuio2M4/qJ9PbQG9ZpfHVVNCrJVwyx1Ef/NjjUyKg99+APbRCW8UsNElU4lMTgN5Iy2AQTk4zgcd9AQ1mo0VfTTCMxzxt4i7kG4ZYe4GpGg3rNa5zrwrnqY6Gd6ONJKpY2MSSHCs2OAfpnQe/rrMaUeiutW6liamr6I0N0iTfJDnKuuSpZD7bgQR3B03ZJHbGgwA41vWs8j++t6DQHGs5zreszoMOs1gOdZoM1ms1mgzWazWaDNZrNeNRV01GqtU1EUKsdqmRwoJ9udBxPcKKmk8Ooq4InxnbJIFOPzrj+LW8g7a6mYgZwJVz/vqJda200xzWLDLJjG0KrOB747gaXKinsSqZAagMAcNKqhT+caAtUdQW6oRXnts8qqcqzxodp/LcaEyS2WSn8QfNrMW3LNLKkzLznA3sQP214vJTtEnhiPZnG92lC8+gKrrqmqKJJTHOZmTPBpqiVwPoQe2oI92WAjZLebnFIzMWBETEZ9DlsgduAQDjtqJaqapo6cNTXl5cjwwBEkTNk5IADEBf9GDnU6vrlhi8aKqmLMcLGkhZ3PYAAjJP215pNeAw+Zoq+ncuoQvKdrZ/wBKnGqjmrvNSp+Qq5pG8PymJpDCBj3YEs//AFgHRqa9Vs1O6UztEygAuiBjjHcZ4Gf/AF/bUKK4yFBiJ6iYuVwatSpA+jOG/cDXNHcIqbxpJbZmnn8riKRASfbJk0DnQLN8hB8yVaYINxBzz98Dn8DVRdZSQzVUl7t1UBbqyRqeshZcPHVIQqlW7o2RkHt5frqzbbf7fLF4IX5bb5VjJB4xn+nI1U3WlMtB1BX0wVZrbetlUkLjAZgQxIz7OO3H68euin3oTq9rtSRW66SR/wARVDslX9NSo4JHs3bI+oOnbA182WeYS1KUsNU9EfmyImkcB4JN42he4GAp59QcHGc6vDprqQ19sqEupjprhbzsrQTtXtkSDP8ASw5H7emgNQW2hpXZ4KOCJ2/UyRgE6laXW60tkVZBBUR1VOlQrtTzTRbUm24yF5znkY459Ne3z95r1BobclLE3aatfzAe/hrz+CRoJtfaKK4KxlhUSkYEyDDr9m1409pqoGYG7VjQkYWNtjFec53Fdx/J1FKdS0EglM1Jc4SfPEI/AdR/lOSD9jj76IW+70tyRvCZklRikkEo2yIw9CNBP1hGdZrk89sjQVnSyQ2XrCthCustJcPGL/0/L1G0FfoN/m+6nVm6q3rdPl+sK2fckcb2R2meQ8HaxCDHvuK41ZNBOKmipp1bcskSuCOxyM6CTjW/TXPOBrf9OgzHOdYQDrBrOdBsazWtbyPfQcZyQDrN3b1yddcDOsBBAI0GA5A1pTkZ11rX20GE8ga8ZxFL/LdI3cAlVfB50tXCHqiiqA1JWPXq7E7BTxIsY9BkkE6G11F1Lc4kNTZ6V5QCN7vHlefsdBLntN6ecy7fEZhkj54AY/MWvIWW+SxlZackf4WuII//AMtCT0veY4jJ/DYcgc5mQAAfRVzrqhqbnQFvlpFgBADBI5CT7fqjOgKpZL3GmwKqr32Gvbb/AGjGvR7BeHpzCsdBDvPMvjSOwJGMjgZ1CTqKtSXJqKidgRmMqFDfQnwuBo3b+qY5y5rKY06gceGJJCT/ANA0Em2dL261incRmoq4jn5qc7pC2ME5Pbj20Z3cn2xqJSXWjuDlIHkZl/xROo/cgal+Gug8njgkcq8KNuHJKjnVYVFZQx36anglggSGoenhiVgTkYzgeGT3J9dWqFAOh9xstLcLZPQ7FijmO5iiDvnJP300IhWOjl+bmp4ZYk8zeMxUft4WdSOojafiFYzDbayNLnStinfBA8Qrkx5OMgjv+Dpgi6GsomWaohNSwfxNsmAm7OQdoAHGjsdJBFK0qRIrtjLBQCccaJj55lkpqy4JWMhp7zSSiFgRgvksrb/8yDB3Duo++GW3VM813W60twQ101Oiinqk/k1C8lo3x/VuyQ3vn00O+JsdTb+t0k8FqWoqir01XCD4c4Ug7JFPZxjGfUYzpa6eekq2mpqqf5dI51kCs21zhyMKM4U8AemPL9dBfljr7P1bFSXiOKNqukDJsY5amc43D78d/bTFkaqWxtVyzUz0z0xq4qeMJcInIfwznYZgQBIv9J9QefXVkWe4m50haRPBqoXMVRDnOxx3H2OQQfYjRRHcuO+la22ujvkNbdZogJqmocxzJw8ap5FKsORwufzqf1BMTSC105Y1lcpjj290Xje5PoAD+5A1OJobNblQvFTUsKbQGIAAA0Hh09Vy1dkglqJvFlUvG8mMFirFcke/GimQdLdud7f0dV15jZS4qKxUI5AYs6j9iNeHw+nkfpanpZ5mlqKXys7d3VhvVvyrD9tApfEY09T1tFbpmfxKyyVEFPEneaYsNi/vzz7Z0f8Ah7eJPlI7LPGFEMTNTEKRhFcoyNn+pTj8EaU/iDMh+LFr2zvDPSW/xVkTGULSBSeeOFLHnR+z/M2u8xVFUVlhhmqKSqqVIBSWWRWQkexG3n3bQWPnjWZ1DuddHa7RV10g8lNC0p+yjOhPRFyqr30db7lVyK9RUoZCVGAMscD8DjQMWdZrWOdZj66Des/Gs1mg5APrrTJlgfzrrcDrAeceug52kHvxrrSxdem0/n1i3C+NKx3bKarOR9FU8aWJqCsWmLwy9Z+K4IQPIuAR2zjkDTRZbA7yQP6dB7vFfy6vaqiAJgho5Ys84POc++NKlVY4Ka1QG99XXekaXDeD81z74/Tu++gNVb6KS5xyxXTqiO2lfPVt4wjT7Arkj65xoGOW79bxyNG1IuBxuSnJH41HgjutdVlzakFSxLF5aVUyfqSn/fSvV2mzxSBaT4l1DLt3M0t0CkfjB1BpLNcJp1+S6o6kr0GPGeip3ljHth2K5/AOqh3qIbvFJmqtVvklJBBeAfYHIXQ2orpqFl+Zpo4Azbd0KFRn2ySuvO2dJVdzqZY6fri8w1MYPiU08TJIoJ4bDN2+o411WdI9ZW1lc9Y1bw79ofw2Of8A0Lk/30Hgl1R52ihoogsbbSVkMeSftUDOisfWVfRwQ0tHHTr5tmJCrEtk+pnz++kmrtXxIjqgtPf6yqgXGX8KRc+45TUGWk6yRZd15jaVRvZzGNqj058PkfXThbViTdc36ldophRh8A5Ean8/87U0/EaejpoXrLfE25eXSqUE84JK8hf31UzVfXcUMfh3ahZQeW2RHP8A+mTqS5+I0Uix1NxpoJHGUVqdPN7YHh+unGdq0ovilQSVAgNJKJD6CaM49eeeNe3/ANRomhWVLbUNGxID+InJHfGDqq4+pPiBLS+CPD3oADLIISWPP6VwDjjGon8b+IsUhSeNZQUKr4awjYT69vT21NjX6s7qqvTq7ou6bLMJ5aMCVYpuW45JQjswAPv+dUMtVJClVK8CSU7yj/nEjxF4yR6HsvB9/wBm+t6h69tNvguIqKulo3xHUkQxMA/O05C9j2+n50sXSWaJ1mZJU+blbxUiRTEr5GWXB9ePKduDjjQGemr7QUFuMMzzLFUQgANmRAA5wg9ucZH1bnkatixSNHZIL5DdGp66YiI09UQUcglfDb17ghW7gcc6oiSaeOtmpqWJpPCJyrEpsBYclTjHocAZ7d++nTpHrR6Cve0ClWaGoZEWQzZDtglFBwQCSe5xqkWrderqxKNZKOhEdWknhVLSAE0w4znnnPcehGl6Pqd5K5qiO1LeZS/kqquZEEeO21MEIO/bk+ujle892mmq7JB8v1BTUgJ+ZQNFUoxOFOOG5GQR2z99I73frWVIJZZLGRNnKmiQlMEgjk9+D66BzrOpb5N05fnlookWClk8OamdXQEKeclsn6DaNcCT+DdKW++dNZaBaVIJo3/mbkHAfvyykn1xgn2GlLqK93u3dJx09Vc6eOnu0/y3iw0iRCBQPNnaeSew+gOjvw2rqatstV0+rRmFo2CiIN/K4wR5ufY/ckagX7VFU9T/ABI6lWtaN5o6CKkaSXgRgyKX52gA43YH10yyiZaOsnnlLwXCiqRIvcB4T/LcD0OP9h7aT/h5PPX9U9TW2sjczVDvDOwDt7rnjyjBGct+NO1xrIz8P64S08cc1ut0TiTtnd+sfTJT++ipHxKv60XRUVvdlNddfDgWPPOCRvP2Azo50ippGu1rCqkdJVFoFUYAjkUOB+5bVZdO2yfrCtoeqb05ee4VYip4T2hjQl2AH+lBz67jq0unWMt56hklDJMKtYwhXGI1QbCPcHk6BhzhcnWixA7a61mB7aDnd766/GtYGc451vQa2jW8Y1mlOsrLnX9Wz2eG5vbRDTrURhKdZDOhOC249sHjGNA1kZ15zSQ08LyzSLHGo3M7tgKPqT20tNZOpJSpHV7IuOAtBHkj3OdAuq7lXWK1VFBft13tdVCyS1KIkDRZ9sthj68dtBI6hu9B/Eo7tZHNfcaGMmdKdDIj0+cupYcBh3AznP31nVFtN4tcfU1nrXlRYhOiiRgNv+JSvtySpyD99Vl8OPiRS2261UNzqWFJIzM0jn/mZ4yVH9WMDAz/ALnVnWirg6KuE1lr2EVkq5t9rqG5jUvy0LH+nBPGeCDohT6bp6q4xVlwhpLdXXu2yhJIJ0XFXGVyjBscSckZHBxpipepbvf7TKbbb5LZeaXhKaZgYpwpUuq9uRwOQMZ0idb0116E6znulsgnks9ZGEkVRwo7jaR22nkH07fclS9bwX6+WOSgp6qkqp6qNayUxgDeyMvlHruABJ9ABoCV46rrrrE15sVGJJ7KT83TupE8RDc4x3Vl3cfTOrJsHUFu6jtUNfbqmOVJEDMoYFoyR+lh6Ee2quktl2sHxSq7bbq+np0u0STxtUA4mZQFYHb69zjPOdSejenKa3QXmz3GrNNcrXV7o7hSnY5jkwynHqM54ORoLDu90ltBE80QlpiNqrEMyF/qCQNv99KT9Y3FImcUdNsAxtaFhn8gn/bXtUdRT0VtaW9UFPfbdTni4UYRz3x5oichs8eXOpdlqOmuqlq4qSh+XlpSYpopKcRupP8AVjH07+nOqBf/ABtXFHIstK+D+kbhn/8AXXo/WtwZgXs1Nkcgszcfuo0eXou1RiUAS5cFQzENt+oyNR16EptpAuNXkj/BEcf/AKaigM3UtZWQmJrHbk3jYzNUbSAfXOBjQyOoeNJEW1KrA8FLoWVsH2BJ05J0NRofENwrCV7grFg/jZqLMOnFqpBNfaUhSQYH8DCntjG3PB/20HhZKY1dNJDUQW/5OrBSeCetZ2x24QrjP51Tl6s1z6X6hmtV5ZG+ZkzRTNTmZGTJ7Hlhjdggg8Z+mreoqbp+jrY5/wCPWSRUfOPlYFdsc43A9/rjXPXFjsHxDpIIKK7Ugu1OS1M8coY/VTg5wcadHz9Xp4byswppJ49skgg80Z2+Xk7gcYGSAO4HpjWyHqKGWGNWStB8WCMRiPcRg7+ecFAPXuD76my22W3UdyguFKGdXKpup2kAYFlOxs47juef2xqA9sqVpvGQeK0EufDcgLHjAJKk+Yk8ZGRxjRFwfDK6STdL1l3kkWarWJVjpQyhFTIUsQCdpLA+3btpnqrHaemamStrYYXssitK7VD7mgl74XPJDc8cnP31UHwwnqF6qa0mqqIaaY/OVPgS7QoUZGcYznIGPr+zv1jdpb78ZLL08/ifIUBjqGjR9u6QkEE/bI/vorz6y6rj6sszWKksFTFRoqzfNTph0AICtEikljkgfvr26O8a32Uz2O42irnC4mVqVhVE8bi4MgxjAzj20g9QXG72jr6O+PJ8vGlZLTiUMWCqsrgA4B4xxx6A6sat6QXqWwV88FvMjS0nzdBcwwScTHJaJsYJGff7aBbtlI9N1PV3603K21ySHxKykpKgiVGD7t4jZgGP0ydMHxM6utF0+Hvy9pqFqK67yJFHDGP5hCsCQw7jHbB99K3Q9LTWvo+qpqzp5JJrjUCkqKyWoT+SXO0Lt5dWBPbHPvo3N0NLH8R+nzXUscYkp3WeeA4EjRdnwOxZcZH3OglV81bR3Tpiy+K9DFR0iTVax43B3IJQE9hxjjnHA1YfTbvU3bqCcIUi+dWLbuzuKxrlvpnI4+mq5rFpeq+vGuFnukM/z0fgNF4pVqMxg5kZR3HlGBwCTzq3LNR0dutcMFE/iQ43eLu3GRjyWJ9STznQTwDwT31og+h1mfN9NbzoMwda5x//AHW863nQZpY6uoK4GkvNppxU11DvDU+7aZ4mGGQH3yFI+2mfWaCg6nrL5KmgamnqnronmVomyZACwIVx3/qKn6rqvL71tdLvZaehmlkENPvRWdzuZGXG0+hwMD//ALr6O6q+GXTfV0/zNbTvDV4waimbYx+/ofzoHbPgd0tQ1PjVTVVeARtjmYBOO2QoGdNMfNXydZbUpa+SlkjjZfEhM0ZCyAHuPccj99GLv1pcLvY6W1NPKlJF55Yt4YSPknP9/wD5ga+iPih0B/xZ0zBFbUhirKDmnQgBCuMFPpwBj7a+ZKOwVl0rTSUcMkky/qVASF9OT/30iG/4ewdadT172+0XergpEX+dLJIWjjXsBg559hp/6Y6Wt9p+K9PY0nnm/hcPzRklk/5srJjIX07/ANtas9+n6W6VtzUtnqLbDRsBU+AVnjmJ4Jl2kMG9eeNEBeqWP4w269UkiTUF3olQTAY4yV5z7MF4786HDr1fRWm4NSQ3APDOhL0lXkqscvYAkd898dsDnST03S3fp7rcz3mugrqm9ogYQqWjkXLA4OMZUYPtgnVtVFNBVxeFUQpNGTna6gjQm49NU1U6VNHI1FVxReFG8X6Nn+Bk7FfpqLhNv/Rdoqr6lTaWmpno5Y4qykpBgMj8hwvrjd/vonYLZHbPiddKenllkh/h0csgfBCyPIe332k4+p0As/U72Nb9NXpCtxofDoIYNxLPjJDMe5UAjzf4RqwOnbJ/Cop6moqPmrjWsJaqoIwGOOFUeigdhqg0VU+moNzs9DeIFhroTLGrbgu9l5/BGvS41wt9Kag0884BA2QJub740M/4qpQpJoLpx6fJvnUA+p+HVhm8MQLVUgU5YQVDjf8AfJOuKj4c2qWqM0VXcadc58KOpbb2xjnP31Ol6uhVQ0dou0oPtTbcf9RGuYesoJlLC1XMAeoiVv8AZjq5TiAPh3SoJdlxqsu2RvO4KPYA/wC/fjUO/dN1lls0FVZGmmqaRy8qRDDzL/lBOMj++jtR1JUSUVQbdaqk1YiZoVqgI43cdlLZ4zqpF696xuNVKK+tS3qG8M08KrCUYHkF3zzx20TgFfZqq+vMxkWFaoCSaTwyQ2Dhlbbtz2GQoJOOe2gMElLTRVQqadahXDwxRndE0fblCeMem1ucE501VdupJKxpnqq+pedWZkkKS+IxHBKg449PX1PA0DSiWkJcPVy036QlS4IYE4LhAfXzcDAxnQC+mrU1ff7ZCJ2MS1KRySeEMxDdwDzgkkY5znHGrPv1srqb43Qw25Q1VW0UXhzOvljC5DOffG0ceuvDpCMVtwqrgY0emki8Uq3cshUgKsYAU8ADvnt76suzz0rz0r3Onpk6ipYBC8UD+I6RuR+ccAn20FJ9ZWpai8GhsSXiouVulaSsirVDpLuJJkVMngn2XGDpm6Q+KVLQFLfVQSxRZCzwDDJA55zG3+EnPkPI9PbRHryz1N8e49S2Txaa5WmdIUqCdhRY95lI918w++NJkhpfiPYpZCkdr6qQIIxEdqXJSuQGHYtwfzoqz7JJabDSXW410lPWVQlWZpI48TmI4KF1PIIz3P76K9QdQF7ZD/B321FXGslDVugMLtkHwyfRiMgA4znVD2OprbhUQ0stwajqKQOqySSbfBwT23HlDggpyRn1HGmKaa42m4R2pp5KWnudPlaRm/kh2GRJGD+kE/8AQw9tEWF0Ej0N56ksNyhR6jxBVtJ4IUSrKOQBzkAjGs6JuFXS3qS0mmSntc7VUlHDtIeHZKAVP0w3A9MaG2y4Gl666buNQk0Vbebe1PWxSqVKyLja2D2yQRru5z1VvvtDVRSqKmleeLH9Eksis7jHqAxiH76KtIDjWY0F6UvUl+6ep6ydAlUC0VQg7LKhKtj6ZH99G9BmNZrNZoM9NclwO+tngZxrwq6mCmpZaiZ1WOJC7EnsAM6BZ6u+Ilm6PEcVWZJ62UZjpYRljzjJ9ANT+luraLquilnpopqeWBgk0E64eNiMj+2vme5XF+puuJ66pbxpKiUpEIgXCoBheO+AO+rAtHVlJ0k15rwqxSPQRCCGSAQb5NxCnYO47nIzwO50xNWL158QbX0dapfEkWa4un8mkRsOxPqfYfXXzpYqW5z0galuE9LPUVGHgikUNjvu2bgzc4OMY1BRrj1N1S1RWeNUVFRIHlOW4B+wJA+w+mrVttuhqaV4HV5IYn3HxcPGMcYKSKAp/wBTE/T01fBAtl1vVPXpT1YhuEwOyN3ykuD5cE5ynPu2DnRK/wBhp6y1xXizypFdbeWka1SYVwcDxPLxhhjOVAzjPfnRGk6Tqqmrpf4cJUo1UbIpiT4SlsuyMwAXj+kBhqXfKeO3dX1Sz0Arfm0RB48Yy6gcbGUZyMke/wBPXQGbP8QbH1L07BPUVgo5jtMieJtw4IPfvtJ/tqv634p9WN1CbXZpae4zNKVjEUQ2PlRwpPPBzo1Z+nOkaUr8zZI5aKJsNO4y8BJ/+7jhl9N3ceo9dMnU9spbVQWl7BbIIga6J2emhHKrkgeUdmPGfrqBXtnSnUPVUUwv9nS3108+6tuUyIXMYAASEL2GByT/AHzq5IgsaJGvZQFH411jIxqPUCf5aT5IwmpA8glJ25+uOdFQeoYxPSRwm1NcSz4CBlCx/wCZskcaXv4FarZHDBX2hLhWTsdgoqRlUAf4juIH3J0wo1yit0k9yegimRtxMZbwwg9yec6W7D1RSUtY1vm3iOWQsauWu8aME+gYgY+g0EW/WOgtUrPNTU0dDJGdkjQx8OeQvOeeO541EbpyeWHxUtktPAq7nedaSNUAHphD++ni2WKhoWlnpZ6ibx+S8tS8ox9MkgD7a6vEMfyW6a7PboEOZJFZFDD2JYHGiYTrRRJUR/OWyGlmkgcGQfyQMd93iCPH4GgfVtdZ7zVCrt8Faty27KiroZG+XTHozhcOfqBn66b5+puk0rab/wA5k3BNipG7mORR7gDDffSrX9FWW63T57pW7wY83i2xanYrN7qMEpz6Y/bQ+F+CgmYRSXGskq6zwQqwglhHuyvMe0ct6ZPpnQy8XGnQ1EpaGKNFhpwTCQiKvA28HIB7k+/cYB1OhlrpxNFW0tDaI4HaIo07MWdfdBnOefMR6+mhFzXqYLNTmnCGMq2SoJVQ4UIAwOBl8Adz66qJr3YW6aG7UIimNKUDOgcM4ZiWAyz4OAVBH199WDR3Opj6Ue5z0tO16kpJKqkeEk7FlYDzMfXOPwMemqauU9VS32tMMwpXjmWURTxgqzrgKEUeU8AE6tO036K4WmgpK6tt8BkrYmryrEDbjeFycDcXUAgcZJ1Fh3pEtcFnns9dc4DVTBjWESBCXk5bg9u/H01SfxLt9PYOu7fVWqQLA9DupWgYDwjGpC4IzuwQPvq7rla6i5p41VRxyiKU7KQSr4cy54Z8p3+mqG+JV/o674mUiU8MdRS2xEgMSjKM2clRj2Jx+NFGOg6KXqiWuq6LZDdImSVht/RKVIL4PoWUZHs51Y3VVkTrHo6imroloLvCw8MSg+WTGHQe4YA4/GlpukzZvilba+3VQpKSuUyVAx5UcbT4Zx6sSvGmmqWqrLvDUx0UktZQShq5IpCIpNoIXaOxfDbgPTsfTQB7/VyVnRHTfUNWoIp/lp/FA88UgZckn1VhkH640T61gmq+pbI1JTxVM0G6sjjckAKgJYkj1JKAfUa87nUy37p+upDF4NnrKuKipnMRjaNONzbSPRwRrVvviJ0K9yUCe8xJ/CeDlnmUlVA+5Ib7aBl6OpxHaZ6pFCRV1TJVxJjlUc5Gfr66YtLvRLVEnRVqFSVNRFD4TlexZCVyP20wLu9dB1rNaGc/TWc6DNVz8Z7ybP8AD2qSF9stZItMDn0OS39gdWMQDxqo/jzb567pu2RU/IFUXYenCHSD58stelJXNJKpYbCgXxmj78ZLAZwO/wCNMfUdUl221m6bcseVMsu8kHGCCfXJzj2740CoqSeFdkcbQ1K7i8hbaMDkftg59+NGIbVNcq6CzQI/iTlXldSMBRnn0yMEEEkaqDvRlNLaKVrgwg8eoQur1cQICg44YMCueefX0zq4OmJ7I1O5rxS08scRdBKGBjA7lSzMuP8ASfvpW6Y6faqLLUJWrTUCESlHKCR17bWDYDAd249gNT+qrlTwdPvPWU0Y8NonpoD2QK4bOD2yAe/LcngagbLdUBJHnsdhqqlXU5raqbwzLz2BfLEfgDXN1prp1DRNQ1vS6op/TK9cnkPuCozprptssEc0ZGx0DDHsRn/vr2YqEOWAx3J0VXzUB6Oo3p5K3xqqudxHLJGz/wAoDOw5OM+mT765sd3rrRTYlkhrLRABlIkIkpYj2bn9ajkHgEYPHGiPVV/sklukppZXmcKZYmgXcQw4yPcg9x7HnjSrZpKmKaO4ULyAADfGYyRICNxGD3yAcc8kYPPJIb/iB1O3TPRNVdaNw88iiOmxyCzdj+Bk/jVHdP2vquaroLilfX00dTVrSiqiqCxaQtyWRjn1I7Y8umH4hW6qrKy32ikmastk6mWmt8coZqWUEbgcDcQN3HsM8akdMxUtG0dtqo6OtmpUJVTA0MzRgllKk4/mK+QRgHvzposy136qPzlmqljqr5QgAop8NalcA71J47Hkeh++iE9BQ11JHX3m2pFNErZjeQMAo9Dg7W9+dU9ceorhH/DL7QySyVUUkMskDbV2hoyjEsRyG8MjuPTVxG32a/RU11elp6wPEGhkdQ3lPIxorysN5oLoHp7bCYoKdAAPKoXOcAKDxqpeob3V9Z9U3WkoLfUXGjom8CEqu6KFv6pGXsxzkY9tWd1Xc6npvpC6XKKKJpkXbAI0xgHAXPvgnOhHwmuFgbpmOgtrba6NBLVh12ySO3Jc+4ydVAm2X2/WKGKlr7StPHSQs89RUgBSM8sGGTtGQMYyTr2sXVtr6xm+XqLSKtgu81NPCQFYk4wTgg8d8+mm6m6u6Vv1RJaluFLNMxMbU0w2sx9trYzpTrDS9D9a0NsoIhQW6vgklMiqoVHX+ndjtznBPHp31FR66209HU1FJFVESTSGQVDgb0wA7ByeA4Kp35I/Oky/vU3JUd5RTULTeHJJ4nl8MOh3574HkBPuDj1Ony/M9Ra3uFSsEldQVLU9TKowJFUlkcj34x9NzY1V1/qWtUCUVPC4qTI/iz+JuWFd69ge/wCjse2fodVEK9VMM4nWjqRDLTvM6rTTF1kVsKqDnnAySQOw0Ga7rCPBj8OSNCs0ScRqsinKlgCSeAwwe2ddtUS1FVUtugeeCEhp0j7qAY8gnGAd24sfcccaEva1SkCBJWqKmUIoCg9+FX6EkNyO+NDFvn4m9S9Z01Fa7RSigepkWmqJy2G3lSW2kjCjg+51W9Z0rW2K/UkFyWojXxQaiZBuA2tlyGHfAwcnVl2S3Vdh6PtFdtV3tVwSeejK4mkYp5jyeMBsgDg4ydenW1Pd4rxHWTUjCm8eOpqWD8JG5ChGUcZyB3/w6gZbTcoFpaehqKXddK6qaopouSkQSMNHl+x8qoTzznWWu6SvXGm+YMddUVzihemUOki4BkLD1A7nPtwdRemrfPaLqJKuKkjhNNikqJ6hmljhbbkbP8ZyM/bHbUKXoe5WmSkucEFRLcKCpBjlRj/MTIDqQOysCTkD76BqU0X/AJZapXqRLRCWSpiL4LbecsvqGLZBGlplXpOtqVo6hI6e57poUcglN4AjnXPszFD7Ag6LdX3+sgjqZ0FVHDNCEiVYyHimiIkYHAzhlOPbjUG4RUl7stpt94pY0EAeETn9IwHRhn+kghG+32Ogsyz0f8Ps9JSbQvgxKpAOecc8/fUzB9DoF0ZcJLl0lbqiYkziLwpc996Eq39xo4GY/wBJxorrnWsnWZPtrMt9NBhGTnVcfGQmm6PjrVAKxTgP9mUjVjqMcZ1UPx1r2FhpLVE4DSS+O4OcbV4A/c/20iVRJuExpSslQzxTgqF3ebgg8/k/nVl9EUtELFW3O5ZZWhdXDTvH/IHHYKRzjHJ1WFvtc9yro6OmVnYvk7AAcdvXtq9rL0ylTYha6xBHb5XAAa6lWYDGG2hefcDjVEHoC4rV32Ou2SQ0reJDDHERt24wowB5gB64znn00I66rJaqT5ZjGxEB8Ibj/OLZBJJ9ABnJ5yB9hbHT/Q1L0/b5Aknj1PgvGh2+VQc4wv2wO+q76gsRvNz8CZjVR0MAWUCQKgYnP68dwcDCg+3GoLO6FqHrOhrLKXDMKVEYhs5KjB/20VutrS7W+ahnkeOKZdrmMjOPznSR0U9d03ZEttNSfxGjp2LgQtiVVYk5CscMucgcgnGcc6c6DqC13NzHFUqtQP1QSgxyL91ODopDvVJRLRXK2WG1VMl2pIWRZ6mLxBIMglctndxggH8aVunfiFeYayjW4wwVUdOTERDuRk5AJKLgEAbu44Or1Vldd8ZDIeQVIIOoj2+kiMskVJAsr5y6xgE5+uiYTrxDHd5Uo2SOOfx3U1sKBSGKgxSKw5DeZP7jVZ9WVZhWCpkkkqKm4W5leJjuK1St4e5P8J3bjx66sy02eoWn2VVXHT/J+EtQXf8ASUGOfTkBGB+ulu7dPU0nQ3VV1ibx6iWqlaOoV8gRLLuwh7Lznn30UsWShmuUNqszywrQVttWSskBxMsiu+0ZOcspU4Xt31ZvwxuRk6dahAnUUz5QThQ2x/MP08d92qJ6dpWRKypnMzSUVQrmWGbJDCYA5HZid3HvzqxRV9SS2WqegZaj5+hXwvCjCSJAjZZQM+ZtsgwePXVQwfEjqLbcLTZoXWWRp/FmgV++Adgb6Z5/Gt/DXp6yWant91+exdbnTNL4UkoG5WIJ2r9OBpI6eod3TMV9o6NMpDUfMy7iZAFY4Vic+bHOfoBo1YZLp1Pa7LFa0pqavsjrTz5jjk8NGAKuCw+nKqfXvqA/1L8KBe+r2v1PXrA7lX8NkJCyKBhuDz27caC/EtayTqq2QB98kVuJ2r5d7l8Hbn127j+NXGDtVVdwWxjPbJ+2qdu9dL1J8QRDC4iSGpNOjuu7IiBLAD0H6+frotau1THRS3ajqFeeS40HzJ2nsUJDfT9W78Y1XtS0EVVLGlQXlclfEVWcqCuTknucgZ/1H306XS40kfWVFI4ZqSGlNPK6f/lLNsY9skMPz7aRLlFVQXGanfxZKIQvLDJuKeKFAOMD1C99GUOoekShrKQtG6lyxqZDicseCAP8G7d3984416dNWoXq+2+milKuswnWYxkkBV3NgE8gFTj7n30ufxSUXBmmkMr+NwwUbjjjhvwO/HGrv6P6PobL0+11vDf+JuB8KJ4nJFOGzggjnHvoopVxytcqG7Tww1aXekMDRwKUEYC4ViTzjzeYd84741Ir6Zl6Kuf8QrEq44YWhEoU+LK4BAD9g2ATjjnvrzt8tILrJYLhuFTcw1RRV6SB4ScZKx+2Dk49dcS9S9IzV81kgjrrjUQ0vy9TNSxlkTC7S5A43YOMj7aoW7Pc6l4pqGupTLNLRP4dQV3OJkJ87MclcjB28cLp4iuc9wvtys12rZaephWOpo6iF9h4XDFB6jnJBz30pRVFf02lskkpzU01ZXVD+NAN4MAQBQwH03HHHPf1020dgirlqBVeDURW6Ax02+Ro5E3YcBnHIABCgg9s6giW8N1T09UU9xuBirqStmnkkjGC0R3L5Qc5Uqceo1zaYLjTdP0NsrKd6kz1kdRBMyZMiMwLbwOxAzz2I1LlFmut0o1nienPil6iJmKmFyixqmR3DHGPQ41zLXSyTV0dFc/maqGOakpVVCjoXkAOT2ITb3HoNAV+GhdemKiJkdPBuFSio/6lHiHAP76cd2k/oSuiFDXUstRC1SK+bzAgeJkhgwH1DDThuHsdFZngHW8n6fvrW4AazJ9hoNEHGdfLXxL6vkvHVdZGj76eBzCgwOy5H9zk6+lOoq7+GdN3KuztMFNI4P1CnH99fF80rR1hqA7eIzfqPcH1P19f30iUx9Loam5ZemkeKRgrMIRIwAySB98fsNXnbOkaIzUqPbq3wuB4zxQQkj6lW3/99VF0VHTRMphWKvlmi3JGWfbRjGXc4HOMAd9W3ZLfMAJamigpJJX8YtU0LMsXAwgYuORjvjnnQNFTYZrXaq6W11tc05hJSKeoaRRjnAzyCQMZz66VBboZqKkuNrEk1qqFDKv9eBx4f0JPH7n01YdrrJa61x1UsaoZAWCqc+U9s/XGONLHw2LDpZ4WRcwVtQEX0UGQkY9uG0Vz0vNFFXgTO6VEikRpt2g9ucd+wAHoFA9SdHrtSWW4RGO5x0cjBgB4hG5c9sHuNLnUMl/ul3mt9poxTMm3fXAlOO4BfHb/ACrn7jXdB0nbOn4mrrxW/MyuQT4v6S325Lf/ADjQai6SrrRTj/hS9SU0DMJBT1A8aAg+inuoP0J1DrOqOtem4fGvVko6ukDANU0TthQeMlTzonWdZyyRypZ6EtHEuWnl4VAPXHGPsSD9NDLD1XdLnePDqKiKekJEXhxx87iO7H8dsDHOe2qgZ051DRdSCvN4oA9PV1jTrvDAeGFCqSvtgD9zo5R22CLpbqu0Rxr8ik06xRL+lFaJXKj2GSf30BsfTlTNRU5oFjkEUklNVKeDC6sQc5PPfP2xpiluQs9q6qrMB4/mwi5/TuMcaHj2B9PpqEUlQT0/8BnijgKGpjwGj5WImdTh8dscf/DptttRJbbxYZbXU0prQkiyQqxbfFjJBHuNjLn6LpOrqGaz0t2oaOZWDzJCZGbGNzFgVA4AIUH8/TR7pipSn+ItklrKNqeGlhMfiNhvEIizu8vdsMudVDLNDXpdeo6Tp62VDWq6bfElkGIInP8AzHUY5BX2PcaX+mLZHXdVz01dNLSPcopIRPC3hujZDqQP9K/Xg9zjT5V3BYrcP4PWzUlCHkenwxJmOcu7Z5EYJxgds5xgaB2+cXm8/LV9N8reWQy0lVGgfAj5KbgoB7cHGRn2OlUa6KqrOkUslBRXauqKU/zKuuqA+0HPmBZhhcA9l0r0bNH1NSTmXdHW3WoWnMeCwWSM7x+CR9c51Y1wtVLH0bUV0VDFBV/w5iUBKLnaW2kcDuT37Z1XFwuEFksFjuFVSGOZpI3pmjGUSQSfzRjsCVVefqdQoWKiWogqbT4ShFMMhAGHIUlZGJHfG3PA/qGmqPomh6ulNdJcJoWp5pImWJ+HRgTtGe36sZ9sjSVS26mkuFTdIoqmqqKuOSoo5D5Nv84qdrdgQGQ+3caYuirc1qqay3VdTIsQidq81Ch1iddrqxByo4Z1444BGgRG6Zrulr+tZcLaqxKZIqZGyRI64XdgHkeYHuPX2xq+OkLhEtloaRhJU+OGcO+0YQcliOMLk8Dk4IzqpOsOsR1VdaK1We0t8lQSPIrIuySTyncwHZRgHjueNF7dXme4zQUjFIJ7PUinIXG1mZSTx/kA/bVEf4gdQ9N01UlL03cpUrjUFpSjb4ISAQWGQSCe3lPpzqN8PKen6boKK+XTwRUVrKtGs0mSYwfM2AODkgDJ798ZzoNbukbk94Wl2+HHJNL45jTxCYkYguDkELg7e+vDquSTqHryiobEGNFGi0lE0nCPw2cH2Y5wdBZtNcqWatulsneOUyiQkRgs0asOKhRjldrYYjvjPPOjTUs0F9lqpjuoauo8OSeEFkkgcKFBIPowx9N2lSltcvUj0V6o6pqW/pRp4WJciR4+8br2CsQeP8ue2vWzdRtippqm31FJUwv41wtzEhPDXDGdM8L5h+kcHP50D1FXNcoxa5YopyamWOqaRRhYEJwePX9IH59tD7VbpJamrudNB4cXgSimaQYBDnAb3I2rn6ltE6eF6KzUUlplFa1TVCepmjUYlRiWfGewPYa5vVfNbLfBeatYIpaeOSJaaN8gu+AiE9jj1PpqKpOpljrut74be3A2GKZTjbHGoDHuMEgemTnV0dGdXRXEyWisq45K+nIEcv6RUxkAhhn+oAgMPfVS2+2xdP8AXECz1EYpa1XSSUx/y5HC5yGxkKWbHHcD66nVFELL/DaRpY8TRF6SqlUAxzK+GiL9wvc8Ybtzxqo+gCBjnWZGknoPrqHqKmFur8096gBWWFxjxAP6h/3Hpp08nvqKVviXM0Hw/uzJgFowpz7FgNfKlRBTTVMYZMZk2sySAYOPY9hnBzr6k+Kshj+G95cLnbGpx/6xr5UgLBlqQywqcDe2SMk4PYd8HP20RY/REFUlMkSrSvSzFfHDoxyqbSAoGc7mOPTOT+LFpy1Rc66asgpkwjCZadSFRAu6QE+rYO0n0LkemqX6TlrfHmWldDkM28Od0Eag5Ye2ew+v31cdmhFvtj0SlZxERE7htxl2nLAn3eVtp+inQF+murrbHcltks8hqqoIY4UQkbj5mPH1Yj6BdTOipKe3V9/sp2xSQXF5E3PgyLIA4wPpnGlewQ0nTFLJXMqvc5mVfEjQsWTPCpnkbvb/APINOFJ0rBcreknUdNDVXOYmSSVQA0JPZEYcgKOM50Ufuk7U1umlSpip2A4klGVB+2qxe4pLU76mWSuqd2A8oKqv2UEE/YlQfbTLV23qDp3dUWqd7zQAea31smZEx6xyHvgeh/fU7py5WK9LPJR0sMNYjbKmBlAliPscf7jQV/XVlzqASKlVo43YQJ4Ww+wYKMAD2yD6nnAyT6SiNBNLVyfzae307zO4XGXIJ9ONxH9se4003bo2C5TNLBUtTHjyhAV7e2u79SU9p6MrKaijRCYxGGb+pnIUsx9Sc86IBdFIb4t6guaiVJavxw0R2bZB5HHlxghlyPcEHUuLptbl8Pqu00TJvkqJmR5GJ3sJSQWPc5x31NpaE9LPf6mnjxSTJ82gzwJcEMMfU4Ogtd1tQ9H0FLY6BVrbhDEDUFmwkRPJLN/iJP6e+mKq7qrpi72Klooa+lLT1NRuNUMEqEB4G3PGCDz226K2OVqv4h0cdkm+clp4Z3EtTIFTH6FY7R7BfvxqfTdSdQ9fXGqpF+WR6INLHGISFRwDgM2TwRkc476H9H0FVLFLGscyV7uKcRspjP6iCrHH6dqAnv699EOFH0HWRFFvfWO2oUkwxQbVVcHdnDeoyewHHfTJ0p07DY553qrhSVtRnbBIkYR44++0jJz6fsNI9b8y9DM1xtSS05Vh8xU/yzlSVwJADwcD9WOB20GpbgbbEXu3TKyUsJAjrLdVKZgpAAyQ3OOAM88AaGrQu9TaZY6emvqSPSyvJKryNsRU5HmweRz6+47ara+0VuusNyo7RW1tTSpKkaJtBjiXzFgvlJA7AH+onR6luVN1XFS0tVNLS2+in8IyV0y+OSBznBILegOOOTknGmcdNUFNFCtrvngKh8RFlZZAT7k5DH07nQV5RdDXm32/5GFKhqespUEn8tI2UZ3NFy2ecnOPpnOgXVMddZLZJZ44JKaS5zComjaXe8NKnlRGbknLZJ1cstouhmM8YsNZOxzvlhdCPrwzaTviBQxUUsdTW06Xm/18Ip0ooQY0ESnOQBl+59xn6Y0MV50zQVjVNHNbKJ6p6d/5q0gJYD+oORwGwcA5P/fTRap547ms3ydT4lNIzyUTw7Z9hAVzx3Hl7f59NnQz9RW+tpLfU9NyUVraPaAsajw277idxOPTByeRpy6h6bp71QSLHiCuVcwVKgbkb0GfVT6j1Gi4pvqO9xW6pvFQkRw0poKGRW2yB9gZvqMFs8dycY0ZsHTdvg+KUM9edsUdFC9p/pSQqm1h9WHtqDX01ZRtPVTW6Ccp5apGXc9LU7Qu9QwIIYKvI9Mds6OdA3+GWmEN2YlonaREnRWdSSSGHJOcHBwBq+p4C0arYupbnaYa8BqOtFbF4jlUVSFJBABLEhivsBk6L/EK11VyobR1nYYJZJUQLPDF5jJCxzjA74P3768PiV0ZWQXYdZ2WqjQwIJpleTbyo7j0OQMEeurB6LEjdK0viRmNCWaGNxgrGWJUY9ODqLhA+H3UFx8eKz3SKspI7k0jwidPDdXJLMY2xyvfjGV+2vLrc09dfaW0UL7KSglXMeGPiSlssS3qfTPPc6KdedX0FuulNLSPLVVNMWSLao8KGQjDEHGS+0nAzj30mUNW8hmRgWJ3yBmYu2QzDI+uHdsHPI1UenVKxQfD/wCZLSrUx1ixU8wXaIymfN+VVfydMkFGOqvh5XUtGwnr6fw66nYhcrIRuwME4JKn1zzz30dvFLFbOg4LLHaZ7rPPBtQGASr4pIyWPocknP00wdH9PL0/09S0jIiT7Q0u0DlsY9O+Bgaminujbg9y60tFQKmNKhKjFVEyYkeV1cyP+4C/bGvoLaPc6WZuloJOsqG6pSUsUNJG7CRFAkklbjnA7Ac/fTP+dFLHxGgWp+Ht8jcZX5ZmI+2D/wBtfKkdF4kbQRcuMytyf0ADt9u/v99fX3UtN870vdKbGTJSyKAffadfINOwjEhdfEOwhVUfokOB5s+mMdue2kSpFuuy2+vjrCi1ck7bnSVBtLg5znjyk44yNWPRdYzQW4eJY7gQzEvNEBtBK+X9PAIQu33OdVtS0sMieBND4cURDvLG6mQxnk45wcAZx/76eempKoWCmtan/wABNJvduS6LuwWQ9skDGCc+U440FldCKL7cZbtUQtFDSnw4oZCM+LzubHoFxsH+nOjPXHUF3sVNTzWyljaFmImmddwU+gx9eedA7Jc6C13+heMOyV8TQ1LN+pZRmRF2jJzy4P11YxEMqYZQQRkqw/3GgE9M3yS/WGGvqaJqSRyQY25Bwcbh9DoP1X0qtTVx36zIYb1AMBom2eMvsfQn2zx6acMRqoACheAABxriSSCMfzHVR7k4Gik7p/4h0lZPHb7jE1PXMwiyEOGftgjuh+h49idd9T3GC5XejsiSRtSLIslwIbJAz5E+hLYJxyANG7jQWO8o1LUx0tQ2N52kb0z2YEcj7/TVfdPdP1dspaaV0ZqY1DSwzRje7xhuGb6kYPPfDe+iPfrFa+x10dDHdZp6K40tRvimQFkES7gFYYwOe5ydI1DZY7jcmpKFH8U7pZqlRv8AELMP0bjhRt/r7nnGmX4h1r3Dq4iIqVt6CFVdTsd2GW3H/CNyA/fQ20VS1zCwJMKZI08WtqOzBGOflgw98E59jqoPxxUFmhXp/p6BhvcfMVIxuqpMdgexA/bg+x171vUNspOo/lhPNJdIpd08kOGMgaNcBSeAAOPf19dD+mdtfVXCSBx4ReOhpxH5RGXJMgX/AEoMcfX30WuNBU2r4gtdbSkctIBClfD4BLRLt8rIB+oYGM4JGor3prlVViT1VK1RcLaziKrDweIy4HmAVXA5B/pGpnUVk6UagqKO8RCOCrVqpZvD2tTgBQTu7g5x++NHaO6VNxrIzRUklNb0bMs1REUMvHARTz37kgduNAOqlpLr1pbrVVALTrTPNPLu2lQTtVc/ViNFVfb6GwU90NleOpeKricR1iKYfE25Knae7Z7ff2406WroHpq7W5qqF6+41EaBHpKmsMYzx3Kj19xwdeUXShhoa6xX2gaSpCyy22vjLEbsZUBskhs47gfTOgHTSX+Gq/i6lqatpsGut8oOKmFkH8wDvnPLffOiD/Vlksdlslup6W3x2yqq5m3SRzNI8axgsdr+5wo/ONRLdd62vjpKz+ORm6QgwJLPCFIDcqpZf1g+xXkqe3fXr8Ua+1R9J9P3G37RSGswqQAElTyw49QVHr3GqrnrVt1xjEPilaeVaiIyABY344b1YAlR7gA++kL6+jenuqHuMsEVRtJmRfDkRcKzbct9hkH9xpq183WjqYpdZKcSolLkiLBIKOUGR9QWXKnVm9P9bxU1zjsdcwjjx/JlmYjyehLMeTyq/fOiypvxBssFwozUU0nhXWCMyqFUHx4lILoQeGGD68jVViyPb6qpq2mNMgDZmEsapkjjsD/0g86va6Uy3W2LJTOhlH8ynk7jOP8AYjj86qCuiuldbaGSOmIgoZd9TFISx3IcFdvbjBPPcge+kSglN1DfYx8jNU09ZSxMJmkmjVGHGAcPyOcAHudRajq69XWumhuN1mipVDI8cQbH2GzBYjB78ew0QuHSd1iia4hPmqGqUTxzKxkVeeCSPXHHmGAMjPA0BqaGmt1VK1TJWLv/AJTmJwQ6BSQoYZ53KpHuufbVQOo2+YtkyyVJMrFRFTuvB8uC3fuM9/Tvjk6eel0nlozU1LxhUO1XC4YOFAK7R37KfrzpQpUlmrZKxmCmI7UV4ginPGCM/p/UvA7ceo0zUtdV2CmarpFR62ohCRiQDYhb9Eo5xnAxj3XQW/8A8QUFvhhoaGCpraqICM08Ee5lYAHDN2B9+ddp1bFFPBDdrZX26edlVVeIyICTgDemRpI+GlvjNTBL820lc7NPUSM0Uu8+vfDr3xwNW8QD3GprUc7M+uteGc9zrvIzjW9By6h1KsMgjBGvkfqS3La+orhTRpiWmrHSMsQQDyRxn6j+3GvrnIOqC+MNrWj6zirwYo4qulLZkbarSL5SM+5UjSJVa0Xgi4KzvPECrArHuIfAIyMkft+NOlh21StBH8rHDKv8iEsMVBUbC/c7HAZ2PPJ/fSHFRrNXTRu8cMBBcNsJ3YPZTg88euM86ZbbLHSmqeSfw6enhZGmigYeJuJUBwRnGGYbhgjVDHWy1C9Z2W5gs/zdWNio/gSRBt6+Gx9wfXVp2i4w2qSZJFiEJfMzxSNIIT6mSV/1sTgbVGdUpcqa89QW+lroFityUtNH4SzFjK+xgd2cdvOGBPBHOnaiuk9RJabxUVnzTOo2pjLK4GJAwPlj8wI4GcAn11BaFVS3Kso5PAuCQu8m+Jli/SnoDnufU/tqsupuh7w1Siy9RU5h2MXqa+f9R9cJ9tWDPeLbXpFTJXvASwaRsFcBTypPpnBGfodAqj4e9L1F7NxuM0dQlOqvFE8vCgZJL8+Yf240ADpToar6fqqO5PdKevrKorDTGLcEMP8AW5558ucfUjRu4S9Q9FSLBBVQV1pnYpTiqbD0oVGbbwMuMDj7a4pr2bxdvFgcwmWaOlpQmAYoD5t2PdwM/QY0K6xqpq+YLJMklHbXNLubI8ebjf29AuFz7udArFoXiqa25u8cu/xWYR7Wdjwe+cckqRj+tfbS61bUVz22z2iJKeWrqCSyHBllc4JPA4XkDGQAPvqJ1N1J89eZQJZfkA44PldiOxb644+u0a3ZLZ1JBUydR2ml8b5KYkTRxbwCQfNkg5XHPGe/OqL76Q6ZprekUFMT8pbS8Ssw5nnIxJIftyo/Oplyr47R1fDPJHIUkpfDkZVP6Qc7h/ix6juM57Z1Wlo+LPgU8tPc1qqacyb3qKDa64A58khO3vnjTnQ3tep6SlSGvgu1I0nmnjURTQ/VgCCjD0IGDntqdD7TvFUU6zQSrJFIAyupyGHvquuq5DZOpI6+vp4p0ra6ER/zNp8KMDAJ/wBZLY+mmS23CrpE8OWhudSUBWN3jjjwvs2GwT9cay8wx3uOKKvtdVEIZDJHMNrqMe+CTg/bRTIx8SAmNhllyrYz+dV9U0lwadrzDk3GmlMEhXZ5oh33D8Yz759M6a4+pLf8tDslNTMwA8OljZyT2PGOBn3xpR6jqKbp6/1V5uN7p4BUwLDDSmPxJsH9QVAefQZPHfQpN+IVqeltUVVaU/8AJpphUKqjiFmBV8D054I98fXVaXSOTdOfPvKoTvYE7hjDqxAxkD9Pfj6avuyXG2VFPV2phLR2kU0coauCrvLjgodxz+nP31WfWHTkdpua1CK9PRyQFmiKnw2fa5DLzwGzwD65HpohH8eRIqWD5GZWiyhdc4OV8x4Bwe3/ALZ0Xob1XVMKSTsspp4z4FcWQywhQOMH9QHb1PJ0NmqZXqllrIpVpwORHHgKxGMEAYHbOvWemooE8KngYy/yy6sdqsDg4XJyxOR6DtnnVRfvw861S7UFPBUyRNUsv8xUk3NvzjdtBJww59AvbUrqm0miqJrhAsnyc53VHgjJikAwHx7HjP1VSeM6p3p6xXCot/zdHKKWvjc+DJIQBId3MTLuLMoIGCRwfpqwulOvrjVRVENfSlpY5EhZp3B8/IKBFGS2AOAPudRoT6Vuk1jukdiqok+Qqnb5WVGysbnnw/bB5IP1xqf1p0dT3enQUlN4FYeI6iJAVU5zhgOR3bzY4ydd3vpiho4aK6UsDwU1FVJWTUq/pwM5YL6MM5474I0Sr7VKC1barw9vll82GIeKTODnafU+40FBVNCbVQzWuvlMcsczrHGeXhJdWPtlMfude9mM1ZVrXVUkQpVU+HHI0qLC2CcgqCeDj9/rq0JY47/UxG6Q2t6tceHPPCUwc8AOM8/5WA+x159RWemp7eXuFDJb6vwyiXC1qzQrzxvC4OO3cfnRBf4fU0cdHM8UgZiA3ErvgNkgeZR/bTwu4cHVc9PXiTp6NYK+LxnkRCzwS52rjghHbdjn0Gnu3V1PcqdaqlmWWI8ZX39QfY/TQiVhhkgc63zrR3cjHGs2n3Oit7c+uq8+MVgF16O+bjjEk9BKswHbKdmGfsc/jVi514VdNFW0k1LMoaKZCjA+oIwdB8gVFHUy1BNO2Fj2FkmkADbmO0YHDBckE9gD6akSyH+CpSwwjc84D+bvkgbc95FwMd8an3m2/I9USWxoDLWUhkTzSfpCjcWwRjlQT/6vpoHUyU4uEdOQngySK43SN4a5475JBGO/340Ra1LHupYoow5jqUTwI/EwPDYEoI2I4zl4yp7canWukpqM/PTQQzWh8GedQN9JKf0zBTwA4C7j6NntoH0/cZyklruUM5kp1aNp5FKsYG5JK+yOQwYc40w0WxaxI6kf8+KSOoWDkAYy2F7SoeXGM/qYaDoXB6atqDEYtuweVh47rH6bmHC5AHJ7DH116dOUdL1FUirlm8KhWRQCWC+MRjCD3BIBIHYBV99Lq264Xe6V1ph6pjfpynCKdiqhm8mVh4GWOBz/AO+jVJFHb4Yay4eJBBRwF1RlESU6E4UhfT85JOqJd3vdT05f26dgoKeoutc++3T08QUQK3lBkH+Xnn2GgnVDW87bPDUsHopNjSeCJfFdifFkbnO4vkD3IPtqDHerjV3h+rZINlXXRsIE3+Wlp0G3xORzljwPUjQyAQ1DyyKGIEfiF1TzFAe+0nK59WHJ76FqBU9MQ3GptdHZUkVq2dopIpJg5fYFy5Izj9RJGT6at2ydO0XTqwJHJcbS29kWNmzBISAAXwSpJPOTt9tV2LjJSWOlkpIDPNTs7eO1RhlG/jAU5i7EZblvc6Z7H1pX01bJTVtSbjBUYxRVTBZY0484JGCuTjDe2c6JKz4qXKGz2SopJaW3m6VcQSOoRPM0efMCMcZxxzjv7aAdKdCxXCOkqHtktQksMchlpp1jdFPbI3LzwTkg6mdcWesvd/t0slMYWqZCIqVSGVaeNAS/iL29Rx76bLDSymkaQ2apSN1WNJ6GqG+IfVfL++Ccaioo6ICSSoLR1AI1JEZW7rhvrjcMa6HTNPTyZgl6wtVSn6ZBM1Qh+4BYEaKC20e0+EnVkZIwZRNKT98Fv+2psc1T8qIbf1OyTICoS5043HA9chWP1PPbTpkKHgdQQV8VPW9SXuelqFUxGnRYZWycEFCpOeM9xxqbe+hqSfpysdbNVRVUBWpFRU1KzTSlO6g5PoTx740SnmO+mqrxerXPWwMQs1JAp+XHfjJLFjjtqQr0dVOtTV/8QXLaVNOrwskchHYhVCj8voqDR1kFTbaKppIaeCemjMVOlUgeSVMZYlRgBuzAA+p1zJSW27V6RU0s98rKidVrZZlIgSDnenbaAO4UZO7HtqPQ093tHUVR8vQxBVUTH5hw5hRwcJkdsFSM5A0RprtSGlip5KmKKp8VnEkJhiMeSTtAJb19froAVz+CdK1zglt9Y5t/iAzUlQxOF5/Q3fjJIznsNJHVnRtLYeopaWheOrMEYkdpRtZGbOxAP0tgc4ABwBjV1SXmtpkeigketurR4jp3C/yzn9cjLwByOO5xxqsa6y3k3008u5riJYpK2Vv0VZYnBx22qAfpwOxzoVLssawWQiZWCKpZ2kjcqBkj1QgDtwNG7bQU1gut06svoaiRhAsUUbkEtgrudF7E8AZPpoRfLXXdP9KUcyU8NDTi4RNUkhWd487jg5Pl3AHGp03W9moEd5aWKutlzqHlq5S4YiEjykL67SGUr3GProh0vl9eilgYRrUW9pFgq9qhvB3EDcxzwBkZBHbUKgpCVlsE0VFXy0UKSwS1MfiIqsT5T6jG04+mNIFgst069ulxMM0lL0rKWgNQE2y1aKwKDn1GMbu+ONWXa7ZaOikjt1ugnmqawkhS+95No5JLHAA/bnRS3fbM1CHmayUtJTTFfmZqdwYXAI/WpQlR/mHA9dB7TVteZZrf0wlcBEokkkNYqKeSNqgqwdfrwDqzoLrDXRzU1VSzUsioTLDOuBt99wypH2Oqy6b6fS0XObqG23Sl8VPEhpqKY7DNEGIVWcng+xx6DRK4vdRXUFB8vWzG3ssi5gmjAE6n0QIWB/8AQBz3GvKPrCrpStVHVXKGmRPPSvURCSEjsSjAFlI9+e3OpPSBuXVnxCqK7qYBZbYhelozwsTMSMgeuMcn3x9NWRfOl7P1HBi5UUcjj9EuMOh9CDoYk2W6x3qz0typyTDURh13AZ/ONEASR21Astv/AITaoaLxRL4WQHEapnJz2XjRD8aK04JGBxrW0hMZ513rNQUr8X+mngvVF1LTb1dkaKZkIGWA45IPddy/fGqUikc7Z6mQgrKuZI1AYh88gEebBBHsNfU3xIraSh6Ir5qzGzaBGCeS+Rtx/v8AjXzZX1dHcqUR2ugeKVshl4LH3wx7L+k8/XGqlNtmu9PSzw1Y/wCbTYFQ0M6vI4xgshPCxgd0PHJAxo1caitHytuipaa1ZQxxzROG3t4gUeD6xOQeffn76SLdSIEo42illZFR0XdGgKhjuKkHDcYGCe5J0+2sXG3JRVstr8WlNWYqSqaXYZVAYruU5O3PP3XjGdBu52G2U9nWeUtboKYF2mUEkqAuAcYJcs+M9+DpUSe+38U8V2kqZrb/AM4UrsFaQg+Xef1bRx//ADvq1bhZTfugTdrrI9RUSUy1aR9o4Wxu8qj/AHOTqtrhLSxuiSF4iAS8UagJux3bbz6duc6qUGuFzuNVX1FMksIaQhWRWO2IAfy1wo24Htkj31zQXmaKo/8AETtHUIx2RpKAzse5kJwAAO2uJKGKuukxVYjEAXLD+WvC8JxxzyeOTrKWlRR8mHMk02WlKAuUbsAwzhjjso99KI8F2H8Tjk8GESqCkqpJtEp3HzcHB4/xE/TTpbqujSiaWnqY4YiCpMnitIrngZA9OO4OMdhpSFnMs6UXyzoinzSxsOO+Sx4B7ds4GmGk6RWsuqP86lVCyFYUznw09yCCSOcg/XUXDRaKOtvtVQM8fjNDHtiq46pmZFHByygbSfYd88jStdPiF1TZeqqqhs90NVR08hj21KK5O3g5OB7cc6sO2dI26ydOz3Z7pW1XgRF8tUZUbf6eAOM68Lb8MIp7MtVPVGOpmjV9/hhGQ7fNkjvyT/300xXVz+JnXcc80tYRCscYfwvCaNVyeOzAnPpoxa/johphBfbQJHQNmTb4oYH09Mevvrx6l6MlhsIqxUS/Lz3BIoEVOJEAYlyF5IyMAewJ9dK8XRF8rVeSC2VKwDCeNKpRFBc8YPp20tItKXreorrZSyWmxU9NTVI3wuxRD2PJAYFeQccc8ait1Tc6NlomvU9TV1EXiApEqpEPRQfEHtjJGdSH6Wudt+Xo4qhAFCbo2VIlEajaSWJJPHpxoXdILhT2+TwYoJHkPkkp5lXwVGOXbHm7/jnQE6a7ERRTx7payomKCeaJpnYheVGD5iBnBwF5OjN8vU9t6VlukMNX4pmjjrJflwjxws2GZeMFgOPpnVbWm9tbL6Iq+CSoiVz4oMoj/pGSHDYIBJ4BGdXhQS2vqbpqopKd98EsTRSLv3lNw7E8++qShlNDHU3iz09pEkVrgiNbUS7hmYkFUDEnJOcsSfYagG+09Xd5/Cs0lwr6uRUhR9qpHEu4B2JOVH6iTj1xqN0TVtDbb101cKZmrrNCYnqEbJmiO4oB+PTR22WyKxXSkuG6WVK+BKd5aggvGwGVGcAAHsfrjWVSKu31Dg1lzSjqJVTw4aQEeFGp4YkvjJI4zjt6aW16apqKqWvoLT047IPLGFDHPqc9gOR2BOnC62ykdjUItHHUEkmSeJXLcdhkjGl64Wy7IY6yGnDxLgskJjy2cA4B4x68HVgnUvUVekESC20Y3eUeFJIkaNntlox/bnSdAZbl1hSXarpbhR19Ir4WKZpC65IHDYVUORwcE+2u61LiBITBVROjcv8AKCRQ3pwMrnBOcfXTNSXyCopY4qzp/wAZ1TaBEI3yVOMbTgqPXkAaIAePfLzQ1ML3eelmPn8Oq8IApk5Taqnk47Z9deNHfJY7TPcr7USrSsj76SGVRKmeOY2HfHYA8e2jVVfqCtn8KKGekwArwu4jRf8ApVh/fGpcV9tMtOsJoTWtACjHxI3VcHtnIHH20QDiMlLJD1BDRSRmJCPnFMbv4Rxnx41PI4zkHI02ydXiOFan+DXKahblaunRJUZf8QCsWx69tCILtYIZ1ngsdHFNjI2TwRsR9tw/vpxttVFWUMc0ULQoRwjAcftx+2izEiKVZoUlXO1wCMjBwddbhrNwzjW86KHXu8QWO2PWzgEKQApcKWJ9ATpIh6xrKisM6VpELtlYcghR7cRZ/vor11TLXijglpmmjVy+zLAE9udqn6+2k7qZqm0dE1hoo/k5ZQsRMrSOoQ8Ns38BsdtEK/V19uPxA6memV9llpd/gLGeJWXPLHBAJK8ZxwRjvoZ1lb6OCFKKCiZri8UZHhR7jhd29sgYxnaPtruxM3THSco+XBudbMEpVcENwRyfYDO777frpusvTf8AA7gtTVSx3DqSqiVnmqgDDb852k/UDso9vTQe9N0BbWtNgsc8AStnZZ5py24ogGTGjc4yBxjHbnR/rqaCwz9G0JV5qH+IhHE0hZj5cAlicnltNHT1robfTtLDULX1kjFp61mDu7nvz6D2UcDQH4kdMS36hStilp1eiikKrVZCKTg+IpHZxt4P10U4y2+BbLJb6eJY4PAMSRqOFGMAaULd0tSX6yUdbukhlkg2TLIWbDjytxuxnI9dFOi+q4uprKsiqwqKcLFUbhgGTaMke4OdSulpGWzvTyLianqZklGfXxGIP5BB/OgSbv0HXwUztRxQowfKmFPEdif6iSpOfrpKuFknsdpqEra4U9TFJinEgKMS2CcNwM47see+NfQ5YBwNeNRBBVYinhjlTPaRQw/Y6GPle0XSm8VYLhVqKJiUzKHUue+d/YDPOAec6bYuk7xdbY1xtMtLdKVmAKwyEujKRn0U5A4xz31Z96+G3SN7Z/mbRFFK2cvT/wAskn144J0h3P4XX3perlufSV4rnx5jE82H7fsw49s6qYmWpa6W2t06y1jR18kcCpK2ZIkBzI7A8qMduMc99WLeFlramlsNMSkMqb6tx3WEcbR9WPH2B1X/AEPSVHW1Vcbp1LUSvWU+yniFNO8IVMZPCkck866uVB1XaL3WVvTni18dK8aPHVTNJJs2BgBk+YZZu+SNRTp1fDFDTWPbtjWK506oMcDOVA/vondWM9wt1uXtK5ml/wBEeD/diuq7PxBi6kqrNa6q31FJdYa9ZpqXH6tiscKT9cDnGnVZK+nvBvFwoDHTmnEKiF/EaIbsksMevH6c9tQG6m2UVW5knp43kK7d5Hmx99LlX0JRyQOkTsxZWDeMckg+gwQB/fTVDNFUQrNC6vGwyrKcgjXegqW4fDImmd1o4lkWMAfLALgD+nAHmz68c6TZb/1N8PrlIbfQmKllwJI6ilcKSoH9XA9xkY19FNJGgLM6qB6k41GNwts7+Aaukkdv/t+IpJ/GdWI+f+m/iXIPiaK2anipIbjhLhwxXyg7XX1Hp/fVqX6Cv6jtdJTl5Y6eZGlmMSsJGjz5No48xGOD250SvvQfT/UCRGoolgmhbfFPS/ypEb3yO/50Dr+hupyAaDq+UtGMRNVQ7mUZUgblI/w98ep0XEWn6f6eT5GGvtN3SOSTZT1VbJu2ynjJGSQWx3YfTXpYeoKO09QJa0ljPjVT0cqIdoEgyUdV+oyrY4yuo926O67u1qegrOo6HDVCTpLGjo0ZX0GPTPPPrplsfQ1qs1dNcpXlrbhMVd5qohtrDuVGBgk8576A1VWylrJvFnMz+XbsErBMYP8ASDjS3e7FaJpp/DtdbFMSvi1NNTqS647Atxj3OnFSjfjXRKHg40FUVkfTtDaxUFKoW8S8kTQxrvx22qOe2oNrr6eeGSWgkSgjmYk/PCN2O70wq8D7nVwmnpyoUxIVByAVGNcmlpW8phiI9to0Fc225KZzBXX2ClypKB6aIREZ4ABUcfnTDSdXdM2mBKFrvRPKgJYU0ZC++cLkDTFFbqCCUyQ0VNHIwwWSJQSP21s0NH44n+Vg8YcB/DG4fnQat1dS3KghraOTxKeZdyPgjI+x1K4+mtIiooVQAB2A9NdaCo/jdLerbbaC8W6QLTxFo58RBipJG0kkHj01U9v6oqb7c4ZbspkpqOAtH4MaoEcDIYqMBj/f74xr6puVvpLvbZ6GuhEtNMpSRD6jVZXz4I2qpgkaxXCrtkrkNt3b4yR247j09dDADoxIr/13DUKuYKGjMiU7yLhJGZjwO/cZxzjOM440MNdeLdTitvVyURzv8x/KIyS43biuwlj6dxjGNeFitXVPwp60pq+8U0k9mIMU9RSL4i7G9TxkYODz9dWNWUPTd5tbU1RUw1VpLl6Gugbd8ozf0vg8AE8Z49D20MJ/T3xBpbdVQzPfJViZ981MypmQegA3ED8YOrgrZaTqHpioFLIk0FXTMEYcjkHH99Ufe/g7fqaid7ZXQXKAyFo2jVfECenOOSfodL/S/VXU/wAOLuIaikqpaJmC1FPMjAEgf0kjg/7404k1bHw36ju09mRJrbDVsi7TJAVjkITygMOxI7emj9jrayHqiaCop3iiqd5IkdC24HKZAJwdhI577RoH0/UUnzM3V3SsArKGtya+3p5ZopOMsozgnjlT37g6h1t0rZvihS3Oz0VRWW14Yfm1hX+bC4LqMoSCOCQR7HQWyGDc6wMDyRzrakHtrRIDYOigV1szVlaKuFaZXQA7pImd8jtjzADQ6K+XWhrI47ksDRN+oHw45BnsceIeNGqlbqa9zFNFDRIocFod+73H6s5+uNQJeo7Kqs1RGy1RXG1IG3kfRiBoEHqG1XK23C43DpK4zGmq3Es8NNzsfBHOBnHsR20ydAXate3V9Vd6WrhleSMHxUZmdggUkcZI8v8AfR+Q2SmSKSoV38QeQvvlP/fXE9httxQ1NIFUFTtQKEUnPqdu7RA++2DpTqm5xfNq0dzQERyoWhk/fjdj86kGxdQ2ul8K0X96iMLgRV6BiP8ATIBn9wdQDFNa4ZUKGKNVMYdQWjUnvtLyDn8a9qWtRbVLNLeaiRlBLSioRCgGMnGWHsPzoA3T9j67tl68Vq8NTO+6eGp2tEQTklNvII+wzqx5oIZN/ijIkXw2UscEe2NKlru9PDTm5Vd4n+XLbYlqKhCHJ/y7FP2xqXNeLZcLfIt0pjKgcFAIH84OdpXIBzgHtoojH0zY4zlbXS59ymf99ed0t9DBQHw7UkjD9Pg0yu0ZxwwH00PmucYo0loa6vWmQKiCOJHzkd8vycY5Ooq9Z0lsfNdcTWJJjwhBDvk7DOQnGM5H7agNR9QU8cKK8FxZwoBzRSZJ/Axr3lvtPDI6PTV2VOMrSSMD9iBr1pLvQVzqlPUK7sm8Lg5xrxl6htMMrRmsRmQ7W8MF9p9jtBwfpoJCXCCZYseKhlUsokiZSMe+Rx+dB4aY1884i6nqZHhOJEgESiMnkAjaT++sq4+l+o5QaiaCaVQUAaUow+wyP31yOkKKlo5haZJ6eRl8gWqkVC3pnac6sHhdKe/0AhkortPMpyCJKdH59MhVyR9cjQ2mvHVFRXSxxVFqZNu7zqVCAdzwT/c8a4n6X6kSiMkt+SndE87mrm8MAHOeTxx7k69aakhktcdviuF0uM/O5oJmEbH6yYA2/wDznRA27dQ9RCYIlUPAYhPFpIw6hu5GMbu3sTr2j6yvVPGz1MdMoWXYscgETOvGTgsSNF4ekq2Cg8LdbZdrmVaeam3KWxjl+D+caFPbqL+IGCsgjir413CngtrOCucbl8xBH17/AE0UZoOu7bOgavnpqYEALtkZsk+n6R/bRJ+qrJGVMlU8e44BenkUH09V0tyWiieAU5hqkUcY/hbbT+AdMPTts8CB52mlkEhwqSLIgA/0Oxwc+2NRB4YPOt6ztxrMHVVmtY1vWaDl0V0ZXVWU8EEZB0iXD4b2mqkkr+m6trNWOfO9JzFIQezpnB59samdYXCerlHT9BbqqsqZVDuY3EccanOC7HuOCceuBpTN7l6QpLZZaOQNBQs5kVGLPUTFjsiBA5GW5IHO0+x1AQfpzqigOyOjSolxgVtsrvlCR/miYFSfrqQ9xvccaCrNzh2nzCrtSVK5HqGiI/fUuTq660t1t4qf4WtFVEhg8jwyIAPM38wDIz9OdGpOs7IJ44IKl6yaSPxUSkiaUlMkbvKO2QdAmUnUFLZ6uWuE9kg8cYkL0E9LK+O2Rg/voxRfECgJL1L2lNz7GaGvXLH04ZVOmqK7W2qMqioiJiIV95AwSM459cEZ9tQqN+muqIHlghoa6NGKsWiVuQcZ5Hbjv21RBPW9AWxT/JvITgK1whXJ/c6mreLmsRnqrKopxyXgq1kOPfGBn99LvUfwmsV0iL2umgt1U3kdkjyjIf1Db2B9iOx0nXfpy7/DWZqmhmq6vpyU4nRWLMgJH6l7DHJDAfQjQXJb7nQ3OMvSTrIVOHXkMh9ip5B++srbbb6xhJWUlPMyjAaVASPydV1RXDpnq54XYTG6Qf8AIkhkVBU++3nDYABKntqZPRUb7o45WaVQB/PEZUtnG0/rwfXtoGVuj7Ca355KNFcqAVjOEODwcds/bUulsVPTRvE0000JdnSORydme4z3I++q0uN5m6euMUNPcaClr4yEmiEEhR88gbgNo4/y86fbR1dablZoK562GNnG148+ZXHBG3v3+mmJKBWKsq7ferrTNTo9OtS3iZUowAHBRSSu3Hrn66zqadKhYlStrhKqFlWBUdmc9l9V4H0Ppp3p5KSth8SCRJo/0nGD+DoGRTRU9Rdqu3SUkEUhkA3ncQvG4oB6+3PGNFJkbUz1k0JSukmjAWNPlVyDtG5f05J7ks2Bz20PuFdT0NRBPwjiUrHGxMn6eSQNmcgercD0GnEdO2jqS1LWW95oY6gCYKhRGlHfDEgkAnuNQqfpGA1dXQRXXw64jx44XgRliBPJAHB9F9PtomFukvFJ83DT3CKoWskkCUiRxxMZWI4UgrkZz6gY00V9t6xoLUaqjmFTOMbaeMRCSFcMSAxUBsnbxgdtLN0+G1RNWTyx1EFL5mqGuFTGUk3+hUjHOAc4986PdJ3uvpquS3QV8t2pI0V0atVop5MjkxkjDL2xk++ig9moK3qijkq66eWlMJIfwFEU4bnIZR2z/tnnTB8O0t1njuEfz1NE1ZVl46TxgzR445OeScZ0nVFyivnWlJcqqplpzNP4UcIbwhBglSjnsWIGSfqBq5noqGqp2i8GneF/1LtBBPvpUj3lp4JxiaGOTIx5lB0CjpZem7gngOi2OYsZEkbApH7gqT/STxj0J16V9LcrfQySWWqp8RoxWCryyk44AbOR/fvqnKybr74lrLDEiG2xNiSGL+SgcHBUk8tgjJGfbRUjq3rK4dS3iop6Cv8ABtdPIJIFQAio8Nu5Pcgvge3I1cPTN1jvvT1Hc4wEE0Y3IP6WHBH7g6oiu6auNBU2azz7o66UPTPHIWCLHu8r7gMBfz31bHS/Rt66ZtElDT36Mq0nirupgwUnlscg4J7aah2xkD20K6gtLXS1yJA5jrIwWp5Vbayt7ZHIB7H6HWrTU3U1UtHc6bzQqCKuIYimz7DOQR6jRfBProoVSWOjijgkEEkcyHfj5h2wx78k86KAEDvoZf6paO0SSG4igYsqpP4e/wAxIwNvrntj66T7deeqYuqJhVUlVU0TpGVSMKi7mON+HwyjCk7efXQWJjJzrWD762M451mD76Des1ms0GtoyTgZPrqN/DKEVAqPk4PGDbhJ4Y3A8jOfyf31K1mgiVdso61JRPAhMsfhu4GGK+2e/roLU9C2ScVbQxS0lRVRiJ6imlKSKgAAVT/SMADA0y6zQJNV8N7Stqitlrp4KKJnDVFTs3zOB6Bj6n1Ptn30OWzXixXusqahbnX0LRxw0otZjh2IoPDICDkEntxqxj31h0AKioKtqJKumqq+CdlJFPXyeIAfTcOT9eCNYz9SMGhlobTMhBBfx3AYfVSp/wB9Hh21r01Ak/8A00sNWBUz26K31rZ3m3Ssi8+vYc4+msp/hZYogBNVXWpQcBJa19oH2GNO41mgWKr4fdMVdvNG1qhRcf8AMTiTPvv7k/fUO0/DqltFEKWG9XjwlLFAKjZsz9hpz1mqIdttyW2l8FXMjFizyuBukb/E2O5xjn6aGVVvuMF2etooqeZTyY5J5FLZGD7rj8aP6zUCFXWjqiuvCTQimttFDncIXLO4I527Qufs3roJZ+ir/QB6+grK+mkmLs8ZdVaQ5G3crEgdvfJzjjVr+o1ntoE6k6dv71EFwrLnTz1CQ7Fhq6fesRJ5YbWAyRgZ/wDfRCvt96an8RKzxJEVR8vTAU6tzz5zuI47cjtpi1h0CbN0HZ7lFJNXWC3GqY53y5kduP6n4Oc+ozqPW/D+lS1QG2QxUtXDiR4VZ2imIH6D5gQCfqPrp61rQV2egTdKCSprBmR48RUEYakjVs8l8MxY/f8AbU6Hoy6WSwyWvpm9fKRvLvHzEIcxg8ttIx3+o07HWaoQ7z0FcL+TLU3iKkq2j8JqmjhcOVIwy8uRg/bRfpy1dRWeGGhr7pTV9HAhRJWiZZ2H9O45wf20zems0GgMeutDdrrWtBDudtp7vb5aKrTdDIBnBwQQcgg+hBAOdLND0Aaa5rWVN+uFaq1K1QjnIPnXO3n0HJ4HfTmO2sGg15sHWiWzrr11mg//2Q==' == basestr)

def test_file_to_base64():
    # Prepare
    basedir = os.path.dirname(__file__)
    img = 'test.html'
    expected = 'expected_output.html'
    myPath = os.path.join(basedir, img)
    expectedPath = os.path.join(basedir, expected)
    output = tempfile.NamedTemporaryFile(delete=False)

    # Execute
    converter.make_html_images_inline(myPath, output.name)

    # Verify
    assert(filecmp.cmp(expectedPath, output.name))

    # clean
    output.close()
    os.unlink(output.name)