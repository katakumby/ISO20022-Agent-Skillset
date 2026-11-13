---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["27 sese.004.001.09 ReversalOfTransferOutConfirmationV09", "28.4 Message Building Blocks", "28.4.6 MasterReference <MstrRef>", "28.4.7.1 TransferReference <TrfRef>"]
file_pages: [625]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.005.001.10"]
---

# 28.4.7.1 TransferReference <TrfRef>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 625 to 625.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 625

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
             Issuer <Issr> [1..1] Text 656
             SchemeName <SchmeNm> [0..1] Text 656
         DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 656
     OtherAmount <OthrAmt> [0..*]  656
       Type <Tp> [1..1]  657
{Or         Code <Cd> [1..1] CodeSet 657
Or}         ProprietaryCode <PrtryCd> [1..1] ± 657
       Amount <Amt> [1..1] Amount C1, C10 657
   Rounding <Rndg> [0..1] CodeSet 658
   OriginalCost <OrgnlCost> [0..1] Amount C1 658
   AveragePrice <AvrgPric> [0..1] Amount C2 658
   TransferCurrency <TrfCcy> [0..1] CodeSet C2 659
   OwnAccountTransferIndicator <OwnAcctTrfInd> [0..1] Indicator 659
   NonStandardSettlementInformation <NonStdSttlmInf> [0..1] Text 659
   TransferExpensesPaymentType <TrfExpnssPmtTp> [0..1] ± 659
Constraints
• TotalUnitsNumberRule
Quantity/TotalUnitsNumber must be the sum of all occurrences of UnitsDetails/UnitsNumber when
UnitsDetails is present.
28.4.7.1  TransferReference <TrfRef>
Presence: [1..1]
Definition: Unique and unambiguous identifier for the transfer instruction, as assigned by the instructing
party.
Datatype: "Max35Text" on page 5403
28.4.7.2  ClientReference <ClntRef>
Presence: [0..1]
Definition: Unique and unambiguous investor's identification of the transfer. This reference can typically
be used in a hub scenario to give the reference of the transfer as assigned by the underlying client.
Approved by the Securities SEG on 27 January 2026 sese.005.001.10 TransferInInstructionV10
Investment Funds - Maintenance 2025 - 2026 625 May 2026
```

