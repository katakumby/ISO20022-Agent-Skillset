---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["4 semt.030.001.01 SecuritiesSettlementConditionsModificationRequestQueryV01", "4.4 Message Building Blocks", "4.4.1 QueryDefinition <QryDef>", "4.4.1.2 SearchCriteria <SchCrit>", "4.4.1.2.3 ProcessingStatus <PrcgSts>"]
file_pages: [92]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.030.001.01"]
---

# 4.4.1.2.3 ProcessingStatus <PrcgSts>

Source: [src-000381](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 92 to 92.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 92

```text
CodeName Name Definition
SETT SettlementInstruction Query is performed on settlement
transactions.
IPOS IntraPositionMovement Query is performed on intra-position
movements.
BOTH SettlementAndIntraPosition Query is performed on both settlement
transactions and intra-position
movements.
4.4.1.2.3  ProcessingStatus <PrcgSts>
Presence: [0..*]
Definition: Provides the status of settlement of a transaction.
ProcessingStatus <PrcgSts> contains one of the following elements (see
"ModificationProcessingStatus9Choice" on page 292 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 292
Or}   Proprietary <Prtry> [1..1] ± 293
4.4.1.2.4  SafekeepingAccount <SfkpgAcct>
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
4.4.1.2.5  AccountOwner <AcctOwnr>
Presence: [0..*]
Definition: Party that owns the account.
AccountOwner <AcctOwnr> contains the following elements (see "SystemPartyIdentification8" on
page 257 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 257
   ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 257
Approved by the Securities SEG on 21 August 2025 semt.030.001.01
SecuritiesSettlementConditionsModificationRequest
QueryV01
Target2-Securities - Settlement Restrictions 92 September 2025
```

