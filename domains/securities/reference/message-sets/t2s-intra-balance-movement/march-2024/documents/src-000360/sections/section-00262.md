---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["14 camt.083.001.02 IntraBalanceMovementCancellationReportV02", "14.4 Message Building Blocks", "14.4.4 ReportOrError <RptOrErr>", "14.4.4.1 Cancellations <Cxls>", "14.4.4.1.5 Cancellation <Cxl>", "14.4.4.1.5.1 CashAccount <CshAcct>"]
file_pages: [318]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.083.001.02"]
---

# 14.4.4.1.5.1 CashAccount <CshAcct>

Source: [src-000360](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 318 to 318.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 318

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         LotNumber <LotNb> [0..1] ± 327
         LotAmount <LotAmt> [0..1] ± 327
         LotQuantity <LotQty> [0..1] ± 328
         CashSubBalanceType <CshSubBalTp> [0..1] ± 328
     CashSubBalanceIdentification <CshSubBalId> [0..1] ± 328
     Priority <Prty> [0..1] ± 328
     InstructionProcessingAdditionalDetails
<InstrPrcgAddtlDtls>
[0..1] Text 329
14.4.4.1.5.1  CashAccount <CshAcct>
Presence: [0..1]
Definition: Account to or from which a cash entry is made.
Impacted by: C17 "IdentificationOrProxyPresenceRule", C16 "IdentificationAndProxyGuideline"
CashAccount <CshAcct> contains the following elements (see "CashAccount40" on page 387 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] ± 388
   Type <Tp> [0..1] ± 388
   Currency <Ccy> [0..1] CodeSet C2 388
   Name <Nm> [0..1] Text 389
   Proxy <Prxy> [0..1] ± 389
Constraints
• IdentificationAndProxyGuideline
If the account identification is not defined through a conventional identification such as an email
address or a mobile number, then the proxy element should be used for the identification of the
account.
• IdentificationOrProxyPresenceRule
Identification must be present or Proxy must be present. Both may be present.
Following Must be True
    /Identification Must be present
 Or    /Proxy Must be present
14.4.4.1.5.2  CashAccountOwner <CshAcctOwnr>
Presence: [0..1]
Definition: Party that owns the account.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.083.001.02
IntraBalanceMovementCancellationReportV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
318 March 2024
```

