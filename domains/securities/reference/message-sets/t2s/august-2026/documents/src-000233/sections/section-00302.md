---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["17 camt.079.001.02 IntraBalanceMovementQueryResponseV02", "17.4 Message Building Blocks", "17.4.4 ReportOrError <RptOrErr>", "17.4.4.1 Movements <Mvmnts>", "17.4.4.1.1 CashAccount <CshAcct>"]
file_pages: [396]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.079.001.02"]
---

# 17.4.4.1.1 CashAccount <CshAcct>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 396 to 396.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 396

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}           OtherTransactionIdentification <OthrTxId> [1..1] Text 419
         ReferenceOwner <RefOwnr> [0..1] ± 419
       Priority <Prty> [0..1] ± 420
       MessageOriginator <MsgOrgtr> [0..1] ± 420
       CreationDateTime <CreDtTm> [1..1] DateTime 420
       InstructionProcessingAdditionalDetails
<InstrPrcgAddtlDtls>
[0..1] Text 420
       SupplementaryData <SplmtryData> [0..*] ± C23 420
Constraints
• CashAccountOwnerRule
CashAccountOwner must be present or Movement(*)/AccountOwner must be present, but not both.
• CashAccountRule
CashAccount must be present or Movement(*)/CashAccount must be present, but not both.
• CashAccountServicerRule
CashAccountServicer must be present or Movement(*)/AccountOwner must be present, but not both.
• StatusAndReasonRule
StatusAndReason must be present or Movement(*)/StatusAndReason must be present, but not both.
17.4.4.1.1  CashAccount <CshAcct>
Presence: [0..1]
Definition: Account to or from which an entry is made.
Impacted by: C15 "IdentificationOrProxyPresenceRule", C14 "IdentificationAndProxyGuideline"
CashAccount <CshAcct> contains the following elements (see "CashAccount40" on page 2832 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] ± 2832
   Type <Tp> [0..1] ± 2832
   Currency <Ccy> [0..1] CodeSet C1 2833
   Name <Nm> [0..1] Text 2833
   Proxy <Prxy> [0..1] ± 2833
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.079.001.02
IntraBalanceMovementQueryResponseV02
Target2-Securities 396 August 2026
```

