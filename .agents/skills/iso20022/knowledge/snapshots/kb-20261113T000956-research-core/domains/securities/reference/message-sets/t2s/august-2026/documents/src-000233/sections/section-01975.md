---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["77 semt.032.001.01 SecuritiesTransactionCancellationRequestQueryV01", "77.4 Message Building Blocks", "77.4.1 QueryDefinition <QryDef>", "77.4.1.2 SearchCriteria <SchCrit>", "77.4.1.2.3 ProcessingStatus <PrcgSts>", "77.4.1.2.3.2 Proprietary <Prtry>"]
file_pages: [2695]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.032.001.01"]
---

# 77.4.1.2.3.2 Proprietary <Prtry>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2695 to 2695.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2695

```text
77.4.1.2.3.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Provides the status of a cancellation request.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
77.4.1.2.4  SafekeepingAccount <SfkpgAcct>
Presence: [0..*]
Definition: Account to or from which a securities entry is made.
SafekeepingAccount <SfkpgAcct> contains the following elements (see "SecuritiesAccount19" on
page 2834 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2834
   Type <Tp> [0..1] ± 2834
   Name <Nm> [0..1] Text 2834
77.4.1.2.5  AccountOwner <AcctOwnr>
Presence: [0..*]
Definition: Party that owns the account.
AccountOwner <AcctOwnr> contains the following elements (see "SystemPartyIdentification8" on
page 3078 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 3078
   ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 3078
77.4.1.2.6  MessageOriginator <MsgOrgtr>
Presence: [0..*]
Definition: Party that originated the message, if other than the sender.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.032.001.01
SecuritiesTransactionCancellationRequestQueryV0
1
Target2-Securities 2695 August 2026
```

