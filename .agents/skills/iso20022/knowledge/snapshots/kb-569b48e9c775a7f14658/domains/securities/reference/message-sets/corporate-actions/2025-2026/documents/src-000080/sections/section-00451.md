---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["8 seev.036.001.17 CorporateActionMovementConfirmationV17", "8.4 Message Building Blocks", "8.4.12 CorporateActionConfirmationDetails <CorpActnConfDtls>", "8.4.12.10 SecuritiesMovementDetails <SctiesMvmntDtls>", "8.4.12.10.15 RateDetails <RateDtls>", "8.4.12.10.15.3 NewToOld <NewToOd>"]
file_pages: [605]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.036.001.17"]
---

# 8.4.12.10.15.3 NewToOld <NewToOd>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 605 to 605.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 605

```text
AdditionalQuantityForExistingSecurities <AddtlQtyForExstgScties> contains one of the following
elements (see "RatioFormat20Choice" on page 1099 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   QuantityToQuantity <QtyToQty> [1..1] ± 1099
Or}   AmountToAmount <AmtToAmt> [1..1]  1099
     Amount1 <Amt1> [1..1] Amount C1 1099
     Amount2 <Amt2> [1..1] Amount C1 1100
8.4.12.10.15.3  NewToOld <NewToOd>
Presence: [0..1]
Definition: Quantity of new securities for a given quantity of underlying securities, where the underlying
securities will be exchanged or debited, for example, 2 for 1: 2 new equities credited for every 1
underlying equity debited = 2 resulting equities.
NewToOld <NewToOd> contains one of the following elements (see "RatioFormat19Choice" on
page 1101 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   QuantityToQuantity <QtyToQty> [1..1] ± 1101
Or   AmountToAmount <AmtToAmt> [1..1]  1101
     Amount1 <Amt1> [1..1] Amount C1 1102
     Amount2 <Amt2> [1..1] Amount C1 1102
Or   AmountToQuantity <AmtToQty> [1..1]  1102
     Amount <Amt> [1..1] Amount C1 1102
     Quantity <Qty> [1..1] Quantity 1103
Or}   QuantityToAmount <QtyToAmt> [1..1]  1103
     Amount <Amt> [1..1] Amount C1 1103
     Quantity <Qty> [1..1] Quantity 1103
8.4.12.10.15.4  ChargesFees <ChrgsFees>
Presence: [0..1]
Definition: Rate used to calculate the amount of the charges/fees that cannot be categorised.
ChargesFees <ChrgsFees> contains one of the following elements (see
"RateAndAmountFormat59Choice" on page 1121 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 1121
Or}   Amount <Amt> [1..1] Amount C1 1121
Approved by the Securities SEG on 27 January 2026 seev.036.001.17
CorporateActionMovementConfirmationV17
Corporate Actions - Maintenance 2025 - 2026 605 February 2026
```

