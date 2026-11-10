---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["6 semt.032.001.01 SecuritiesTransactionCancellationRequestQueryV01", "6.4 Message Building Blocks", "6.4.1 QueryDefinition <QryDef>", "6.4.1.2 SearchCriteria <SchCrit>", "6.4.1.2.3 ProcessingStatus <PrcgSts>", "6.4.1.2.3.2 Proprietary <Prtry>"]
file_pages: [140]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.032.001.01"]
---

# 6.4.1.2.3.2 Proprietary <Prtry>

Source: [src-000381](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 140 to 140.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 140

```text
6.4.1.2.3.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Provides the status of a cancellation request.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 224 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 224
   Issuer <Issr> [1..1] Text 224
   SchemeName <SchmeNm> [0..1] Text 224
6.4.1.2.4  SafekeepingAccount <SfkpgAcct>
Presence: [0..*]
Definition: Account to or from which a securities entry is made.
SafekeepingAccount <SfkpgAcct> contains the following elements (see "SecuritiesAccount19" on
page 193 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 193
   Type <Tp> [0..1] ± 193
   Name <Nm> [0..1] Text 193
6.4.1.2.5  AccountOwner <AcctOwnr>
Presence: [0..*]
Definition: Party that owns the account.
AccountOwner <AcctOwnr> contains the following elements (see "SystemPartyIdentification8" on
page 257 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 257
   ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 257
6.4.1.2.6  MessageOriginator <MsgOrgtr>
Presence: [0..*]
Definition: Party that originated the message, if other than the sender.
Approved by the Securities SEG on 21 August 2025 semt.032.001.01
SecuritiesTransactionCancellationRequestQueryV0
1
Target2-Securities - Settlement Restrictions 140 September 2025
```

