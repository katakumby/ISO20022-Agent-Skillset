---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["8 MX secl.007.001.03 BuyInNotificationV03", "8.4 Message Building Blocks", "8.4.4 OriginalSettlementObligation <OrgnlSttlmOblgtn>", "8.4.4.14 Depository <Dpstry>"]
file_pages: [271]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.007.001.03"]
---

# 8.4.4.14 Depository <Dpstry>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 271 to 271.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 271

```text
Quantity <Qty> contains one of the following elements (see FinancialInstrumentQuantity1Choice on
page 396 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 396
Or   FaceAmount <FaceAmt> [1..1] Amount 396
Or}   AmortisedValue <AmtsdVal> [1..1] Amount 396
8.4.4.14  Depository <Dpstry>
Presence: [0..1]
Definition: Place where settlement of the securities takes place.
Depository <Dpstry> contains one of the following elements (see PartyIdentification34Choice on
page 446 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   BIC <BIC> [1..1] IdentifierSet   'C4 446
Or   NameAndAddress <NmAndAdr> [1..1] ± 447
Or}   Country <Ctry> [1..1] CodeSet   'C5 447
8.4.4.15  RemainingQuantityToBeSettled <RmngQtyToBeSttld>
Presence: [0..1]
Definition: Provides the remaining quantity to be settled.
RemainingQuantityToBeSettled <RmngQtyToBeSttld> contains one of the following elements (see
FinancialInstrumentQuantity1Choice on page 396 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 396
Or   FaceAmount <FaceAmt> [1..1] Amount 396
Or}   AmortisedValue <AmtsdVal> [1..1] Amount 396
8.4.4.16  SettlementAmount <SttlmAmt>
Presence: [1..1]
Definition: Provides the amount to be settled.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.007.001.03 BuyInNotificationV03
March 2026 271
```

