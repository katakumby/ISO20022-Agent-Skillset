---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAccountReferenceData"
source_ids: ["src-000372"]
source_editions: ["december-2019"]
message_ids: []
heading_path: ["3 reda.019.001.01 SecuritiesAccountQueryV01", "3.4 Message Building Blocks", "3.4.2 SearchCriteria <SchCrit>", "3.4.2.3 AccountOwner <AcctOwnr>"]
file_pages: [19]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.019.001.01"]
---

# 3.4.2.3 AccountOwner <AcctOwnr>

Source: [src-000372](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAccountReferenceData_v1.pdf`. Locator: one-based file pages 19 to 19.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 19

```text
AccountServicer <AcctSvcr> contains the following elements (see "PartyIdentification136" on
page 89 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 89
   LEI <LEI> [0..1] IdentifierSet 89
3.4.2.3  AccountOwner <AcctOwnr>
Presence: [0..1]
Definition: Party that legally owns the account.
AccountOwner <AcctOwnr> contains the following elements (see "SystemPartyIdentification8" on
page 91 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 91
   ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 91
3.4.2.4  PartyType <PtyTp>
Presence: [0..1]
Definition: Specifies the type of the party for which securities account data have been queried.
PartyType <PtyTp> contains one of the following SystemPartyType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 19
Or}   Proprietary <Prtry> [1..1] Text 19
3.4.2.4.1  Code <Cd>
Presence: [1..1]
Definition: System party type, in a coded format.
Datatype: "ExternalSystemPartyType1Code" on page 95
3.4.2.4.2  Proprietary <Prtry>
Presence: [1..1]
Definition: System party type, in a proprietary format.
Datatype: "Max35Text" on page 100
3.4.2.5  OpeningDate <OpngDt>
Presence: [0..1]
Definition: Legal opening date for the securities account.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 02 December 2019
reda.019.001.01 SecuritiesAccountQueryV01
Target2-Securities - Securities Account Reference Data 19 December 2019
```

