---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["39 reda.019.001.01 SecuritiesAccountQueryV01", "39.4 Message Building Blocks", "39.4.2 SearchCriteria <SchCrit>", "39.4.2.3 AccountOwner <AcctOwnr>"]
file_pages: [2111]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.019.001.01"]
---

# 39.4.2.3 AccountOwner <AcctOwnr>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2111 to 2111.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2111

```text
AccountServicer <AcctSvcr> contains the following elements (see "PartyIdentification136" on
page 3060 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 3060
   LEI <LEI> [0..1] IdentifierSet 3060
39.4.2.3  AccountOwner <AcctOwnr>
Presence: [0..1]
Definition: Party that legally owns the account.
AccountOwner <AcctOwnr> contains the following elements (see "SystemPartyIdentification8" on
page 3078 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 3078
   ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 3078
39.4.2.4  PartyType <PtyTp>
Presence: [0..1]
Definition: Specifies the type of the party for which securities account data have been queried.
PartyType <PtyTp> contains one of the following SystemPartyType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2111
Or}   Proprietary <Prtry> [1..1] Text 2111
39.4.2.4.1  Code <Cd>
Presence: [1..1]
Definition: System party type, in a coded format.
Datatype: "ExternalSystemPartyType1Code" on page 3246
39.4.2.4.2  Proprietary <Prtry>
Presence: [1..1]
Definition: System party type, in a proprietary format.
Datatype: "Max35Text" on page 3328
39.4.2.5  OpeningDate <OpngDt>
Presence: [0..1]
Definition: Legal opening date for the securities account.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.019.001.01 SecuritiesAccountQueryV01
Target2-Securities 2111 August 2026
```

