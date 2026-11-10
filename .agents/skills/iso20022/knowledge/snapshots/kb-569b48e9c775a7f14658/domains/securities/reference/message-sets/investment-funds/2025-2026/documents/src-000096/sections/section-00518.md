---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["30 sese.007.001.10 TransferInConfirmationV10", "30.4 Message Building Blocks", "30.4.4 RelatedReference <RltdRef>", "30.4.7.1 TransferConfirmationReference <TrfConfRef>"]
file_pages: [712]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.007.001.10"]
---

# 30.4.7.1 TransferConfirmationReference <TrfConfRef>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 712 to 712.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 712

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
             Quantity <Qty> [1..1] Quantity 744
             QuantityType <QtyTp> [1..1] Text 744
             Issuer <Issr> [1..1] Text 744
             SchemeName <SchmeNm> [0..1] Text 744
         DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 744
     OtherAmount <OthrAmt> [0..*]  744
       Type <Tp> [1..1]  745
{Or         Code <Cd> [1..1] CodeSet 745
Or}         ProprietaryCode <PrtryCd> [1..1] ± 745
       Amount <Amt> [1..1] Amount C1, C10 745
   Rounding <Rndg> [0..1] CodeSet 746
   OriginalCost <OrgnlCost> [0..1] Amount C1 746
   AveragePrice <AvrgPric> [0..1] Amount C2 746
   NewAveragePrice <NewAvrgPric> [0..1] Amount C2 747
   AverageDate <AvrgDt> [0..1] Date 747
   NewAverageDate <NewAvrgDt> [0..1] Date 747
   TransferCurrency <TrfCcy> [0..1] CodeSet C2 747
   OwnAccountTransferIndicator <OwnAcctTrfInd> [0..1] Indicator 748
   NonStandardSettlementInformation <NonStdSttlmInf> [0..1] Text 748
   TransferExpensesPaymentType <TrfExpnssPmtTp> [0..1] ± 748
Constraints
• TotalUnitsNumberRule
TotalUnitsNumber must be the sum of all occurrences of UnitsDetails/UnitsNumber when
UnitsDetails is present.
30.4.7.1  TransferConfirmationReference <TrfConfRef>
Presence: [1..1]
Definition: Unique and unambiguous identifier for the transfer execution, as assigned by the confirming
party.
Datatype: "Max35Text" on page 5403
30.4.7.2  TransferReference <TrfRef>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 sese.007.001.10 TransferInConfirmationV10
Investment Funds - Maintenance 2025 - 2026 712 May 2026
```

