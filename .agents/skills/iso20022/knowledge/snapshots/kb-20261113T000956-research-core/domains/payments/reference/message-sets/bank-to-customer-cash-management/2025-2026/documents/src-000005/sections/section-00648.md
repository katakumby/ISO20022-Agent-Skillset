---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.21 Quantity", "6.1.21.1 FinancialInstrumentQuantity33Choice", "6.1.21.1.3 AmortisedValue <AmtsdVal>"]
file_pages: [881]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.21.1.3 AmortisedValue <AmtsdVal>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 881 to 881.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 881

```text
6.1.21.1.3  AmortisedValue <AmtsdVal>
Presence: [1..1]
Definition: Quantity expressed as an amount representing the current amortised face amount of a bond,
for example, a periodic reduction/increase of a bond's principal amount.
Datatype: "ImpliedCurrencyAndAmount" on page 886
6.1.21.1.4  DigitalTokenUnit <DgtlTknUnit>
Presence: [1..1]
Definition: Quantity of digital tokens expressed as a number, for example, a number of blockchain
tokens.
Datatype: "Max30DecimalNumber" on page 912
6.1.22 Rate
6.1.22.1  RateType4Choice
Definition: Specifies the rate as a percentage or a text.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Percentage <Pctg> [1..1] Rate 881
Or}   Other <Othr> [1..1] Text 881
6.1.22.1.1  Percentage <Pctg>
Presence: [1..1]
Definition: Ratio of the amount of interest paid during a certain period of time compared to the principal
amount of the interest bearing financial instrument.
Datatype: "PercentageRate" on page 913
6.1.22.1.2  Other <Othr>
Presence: [1..1]
Definition: Rate type expressed, in an other form.
Datatype: "Max35Text" on page 916
6.1.23 Securities Quantity
6.1.23.1  OriginalAndCurrentQuantities1
Definition: Original and current value of an asset-back instrument.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FaceAmount <FaceAmt> [1..1] Amount 882
   AmortisedValue <AmtsdVal> [1..1] Amount 882
Approved by the Payments SEG on 12 January 2026 Message Items Types
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
881 March 2026
```

