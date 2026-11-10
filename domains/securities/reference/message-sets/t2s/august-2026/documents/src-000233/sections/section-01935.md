---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["75 semt.030.001.01 SecuritiesSettlementConditionsModificationRequestQueryV01", "75.4 Message Building Blocks", "75.4.1 QueryDefinition <QryDef>", "75.4.1.2 SearchCriteria <SchCrit>", "75.4.1.2.3 ProcessingStatus <PrcgSts>"]
file_pages: [2647]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.030.001.01"]
---

# 75.4.1.2.3 ProcessingStatus <PrcgSts>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2647 to 2647.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2647

```text
CodeName Name Definition
SETT SettlementInstruction Query is performed on settlement
transactions.
IPOS IntraPositionMovement Query is performed on intra-position
movements.
BOTH SettlementAndIntraPosition Query is performed on both settlement
transactions and intra-position
movements.
75.4.1.2.3  ProcessingStatus <PrcgSts>
Presence: [0..*]
Definition: Provides the status of settlement of a transaction.
ProcessingStatus <PrcgSts> contains one of the following elements (see
"ModificationProcessingStatus9Choice" on page 3175 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 3175
Or}   Proprietary <Prtry> [1..1] ± 3175
75.4.1.2.4  SafekeepingAccount <SfkpgAcct>
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
75.4.1.2.5  AccountOwner <AcctOwnr>
Presence: [0..*]
Definition: Party that owns the account.
AccountOwner <AcctOwnr> contains the following elements (see "SystemPartyIdentification8" on
page 3078 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 3078
   ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 3078
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.030.001.01
SecuritiesSettlementConditionsModificationRequest
QueryV01
Target2-Securities 2647 August 2026
```

