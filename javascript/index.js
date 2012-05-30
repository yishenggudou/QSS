/**
 * @author timger <yishenggudou@gmail.com>
 * @timger http://weibo.com/zhanghaibo
 * @yishenggudou http://twitter.com/yishenggudou
 * Copyright (c) 2008-2011 timger - released under MIT License
 */
$(document).ready(function(){
    $('a').each(function(){
        try{
            if ($(this).attr('href').match(/^http/)){
                $(this).attr('target','_blank');
            }else{
            }
        }
        catch(e){
        }
    })
    })
