Sub GelombangBergerak()

    Dim A As Double
    Dim k As Double
    Dim w As Double
    Dim t As Double
    Dim x As Double
    Dim i As Integer
    
    A = 2
    k = 1
    w = 2
    
    Do
        i = 6
        For x = 0 To 10 Step 0.1
            Cells(i, 1).Value = x
            Cells(i, 2).Value = A * Sin(2 * WorksheetFunction.Pi() * k * x - w * t)
            i = i + 1
        Next x
        
        t = t + 0.1
        DoEvents
    Loop

End Sub