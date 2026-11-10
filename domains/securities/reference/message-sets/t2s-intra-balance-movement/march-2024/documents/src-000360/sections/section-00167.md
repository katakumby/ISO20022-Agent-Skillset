---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["10 camt.079.001.02 IntraBalanceMovementQueryResponseV02", "10.4 Message Building Blocks", "10.4.4 ReportOrError <RptOrErr>", "10.4.4.1 Movements <Mvmnts>", "10.4.4.1.1 CashAccount <CshAcct>"]
file_pages: [205]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.079.001.02"]
---

# 10.4.4.1.1 CashAccount <CshAcct>

Source: [src-000360](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 205 to 205.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 205

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}           OtherTransactionIdentification <OthrTxId> [1..1] Text 228
         ReferenceOwner <RefOwnr> [0..1] ± 228
       Priority <Prty> [0..1] ± 229
       MessageOriginator <MsgOrgtr> [0..1] ± 229
       CreationDateTime <CreDtTm> [1..1] DateTime 229
       InstructionProcessingAdditionalDetails
<InstrPrcgAddtlDtls>
[0..1] Text 229
       SupplementaryData <SplmtryData> [0..*] ± C23 229
Constraints
• CashAccountOwnerRule
CashAccountOwner must be present or Movement(*)/AccountOwner must be present, but not both.
• CashAccountRule
CashAccount must be present or Movement(*)/CashAccount must be present, but not both.
• CashAccountServicerRule
CashAccountServicer must be present or Movement(*)/AccountOwner must be present, but not both.
• StatusAndReasonRule
StatusAndReason must be present or Movement(*)/StatusAndReason must be present, but not both.
10.4.4.1.1  CashAccount <CshAcct>
Presence: [0..1]
Definition: Account to or from which an entry is made.
Impacted by: C15 "IdentificationOrProxyPresenceRule", C14 "IdentificationAndProxyGuideline"
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
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.079.001.02
IntraBalanceMovementQueryResponseV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
205 March 2024
```

