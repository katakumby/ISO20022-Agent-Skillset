---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["6 seev.034.001.16 CorporateActionInstructionStatusAdviceV16", "6.4 Message Building Blocks", "6.4.5 CorporateActionInstruction <CorpActnInstr>", "6.4.5.15 StatusCashAmount <StsCshAmt>"]
file_pages: [356]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.034.001.16"]
---

# 6.4.5.15 StatusCashAmount <StsCshAmt>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 356 to 356.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 356

```text
StatusQuantity <StsQty> contains one of the following elements (see "Quantity51Choice" on
page 1090 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Quantity <Qty> [1..1] ± C13 1091
Or}   OriginalAndCurrentFace <OrgnlAndCurFace> [1..1] ± 1091
6.4.5.15  StatusCashAmount <StsCshAmt>
Presence: [0..1]
Definition: Amount of cash subscribed that has been assigned the status indicated.
Impacted by: C1 "ActiveCurrency", C12 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 1156
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
6.4.5.16  SolicitationDealerFeeIndicator <SlctnDealrFeeInd>
Presence: [0..1]
Definition: Indicates whether there is a solicitation fee on the event. This fee is paid by the soliciting
dealer.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 1246):
• Meaning When True: Yes
• Meaning When False: No
6.4.6 ProtectInstruction <PrtctInstr>
Presence: [0..1]
Definition: Provides detailed information on protect and cover protect instructions.
Approved by the Securities SEG on 27 January 2026 seev.034.001.16
CorporateActionInstructionStatusAdviceV16
Corporate Actions - Maintenance 2025 - 2026 356 February 2026
```

