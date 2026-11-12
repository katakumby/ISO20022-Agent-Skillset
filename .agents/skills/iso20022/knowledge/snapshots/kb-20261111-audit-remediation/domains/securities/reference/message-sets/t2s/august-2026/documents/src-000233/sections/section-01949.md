---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["76 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01", "76.4 Message Building Blocks", "76.4.3 Modifications <Mods>", "76.4.3.4 Modification <Mod>", "76.4.3.4.1 AccountOwner <AcctOwnr>"]
file_pages: [2668]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.031.001.01"]
---

# 76.4.3.4.1 AccountOwner <AcctOwnr>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2668 to 2668.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2668

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       DeliveringSettlementParties <DlvrgSttlmPties> [0..1] ± C18,
C19,
C20,
C21
2686
       ReceivingSettlementParties <RcvgSttlmPties> [0..1] ± C18,
C19,
C20,
C21
2687
76.4.3.4.1  AccountOwner <AcctOwnr>
Presence: [0..1]
Definition: Party that owns the account.
AccountOwner <AcctOwnr> contains the following elements (see "SystemPartyIdentification8" on
page 3078 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 3078
   ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 3078
76.4.3.4.2  SafekeepingAccount <SfkpgAcct>
Presence: [0..1]
Definition: Account to or from which a securities entry is made.
SafekeepingAccount <SfkpgAcct> contains the following elements (see "SecuritiesAccount19" on
page 2834 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2834
   Type <Tp> [0..1] ± 2834
   Name <Nm> [0..1] Text 2834
76.4.3.4.3  ProcessingStatus <PrcgSts>
Presence: [0..1]
Definition: Status and status reason of the transaction.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.031.001.01
SecuritiesSettlementConditionsModificationRequest
ReportV01
Target2-Securities 2668 August 2026
```

