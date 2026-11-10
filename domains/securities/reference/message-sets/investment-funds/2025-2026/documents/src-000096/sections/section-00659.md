---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["33 sese.010.001.07 TransferCancellationStatusReportV07", "34.4 Message Building Blocks", "34.4.4 StatusReport <StsRpt>", "34.4.4.19 PaymentDetails <PmtDtls>", "34.4.4.19.1 Reference <Ref>"]
file_pages: [896]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.011.001.10"]
---

# 34.4.4.19.1 Reference <Ref>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 896 to 896.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 896

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         Name <Nm> [0..1] Text 921
         IBAN <IBAN> [0..1] IdentifierSet C17 921
         BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 922
         Other <Othr> [0..1] ± 922
Or}     ChequeDetails <ChqDtls> [1..1]  922
       Number <Nb> [0..1] Text 923
       PayeeIdentification <PyeeId> [0..1] ± 923
       DraweeIdentification <DrweeId> [0..1]  923
         Party <Pty> [1..1]  924
{Or           NameAndAddress <NmAndAdr> [1..1] ± 924
Or           BICFI <BICFI> [1..1] IdentifierSet C6 924
Or           ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 925
Or}           ProprietaryIdentification <PrtryId> [1..1] Text 926
         LEI <LEI> [0..1] IdentifierSet 926
       DrawerIdentification <DrwrId> [0..1] ± 927
34.4.4.19.1  Reference <Ref>
Presence: [0..1]
Definition: Information supplied to enable the matching of an entry with the items that the transfer is
intended to settle, such as commercial invoices in an accounts' receivable system.
Datatype: "Max35Text" on page 5403
34.4.4.19.2  Amount <Amt>
Presence: [1..1]
Definition: Amount of the payment.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyAnd13DecimalAmount" on page 5268
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Approved by the Securities SEG on 27 January 2026 sese.011.001.10
TransferInstructionStatusReportV10
Investment Funds - Maintenance 2025 - 2026 896 May 2026
```

