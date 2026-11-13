---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["29 camt.051.001.07 LiquidityDebitTransferV07", "29.4 Message Building Blocks", "29.4.2 LiquidityDebitTransfer <LqdtyDbtTrf>", "29.4.2.6 DebtorAccount <DbtrAcct>"]
file_pages: [684]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.051.001.07"]
---

# 29.4.2.6 DebtorAccount <DbtrAcct>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 684 to 684.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 684

```text
Debtor <Dbtr> contains the following elements (see "BranchAndFinancialInstitutionIdentification8" on
page 803 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstitutionIdentification <FinInstnId> [1..1]  804
     BICFI <BICFI> [0..1] IdentifierSet C2 804
     ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 805
     LEI <LEI> [0..1] IdentifierSet 805
     Name <Nm> [0..1] Text 805
     PostalAddress <PstlAdr> [0..1] ± 805
     Other <Othr> [0..1] ± 806
   BranchIdentification <BrnchId> [0..1]  807
     Identification <Id> [0..1] Text 807
     LEI <LEI> [0..1] IdentifierSet 807
     Name <Nm> [0..1] Text 807
     PostalAddress <PstlAdr> [0..1] ± 807
29.4.2.6  DebtorAccount <DbtrAcct>
Presence: [0..1]
Definition: Account to be debited as a result of a transfer of liquidity.
Impacted by: C9 "IdentificationOrProxyPresenceRule", C8 "IdentificationAndProxyGuideline"
DebtorAccount <DbtrAcct> contains the following elements (see "CashAccount40" on page 783 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] ± 783
   Type <Tp> [0..1] ± 783
   Currency <Ccy> [0..1] CodeSet C1 784
   Name <Nm> [0..1] Text 784
   Proxy <Prxy> [0..1] ± 784
Approved by the Payments SEG on 04 February 2025 camt.051.001.07 LiquidityDebitTransferV07
Cash Management - Maintenance 2024 - 2025 684 February 2025
```

