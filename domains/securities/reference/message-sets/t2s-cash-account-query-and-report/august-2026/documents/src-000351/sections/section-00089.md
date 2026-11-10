---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CashAccountQueryAndReport"
source_ids: ["src-000351"]
source_editions: ["august-2026"]
message_ids: []
heading_path: ["3 acmt.026.001.02 AccountListReportV02", "3.4 Message Building Blocks", "3.4.4 ReportOrError <RptOrErr>", "3.4.4.2 AccountReport <AcctRpt>", "3.4.4.2.10 Group <Grp>"]
file_pages: [103]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.026.001.02"]
---

# 3.4.4.2.10 Group <Grp>

Source: [src-000351](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart2_Target2Securities_CashAccountQueryAndReport_v1.pdf`. Locator: one-based file pages 103 to 103.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 103

```text
Definition: Proprietary characteristics of the account.
Proprietary <Prtry> contains the following elements (see "GenericIdentification1" on page 145 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 146
   SchemeName <SchmeNm> [0..1] Text 146
   Issuer <Issr> [0..1] Text 146
3.4.4.2.10  Group <Grp>
Presence: [0..*]
Definition: Definition of a group of parties.
Group <Grp> contains the following Group6 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   GroupIdentification <GrpId> [1..1] Text 103
   Party <Pty> [1..*]  103
     Party <Pty> [1..1] ± 103
     Certificate <Cert> [0..1] Binary 104
3.4.4.2.10.1  GroupIdentification <GrpId>
Presence: [1..1]
Definition: Specifies the identification of the group.
Datatype: "Max4AlphaNumericText" on page 184
3.4.4.2.10.2  Party <Pty>
Presence: [1..*]
Definition: Specifies a party and related certificate.
Party <Pty> contains the following PartyAndCertificate6 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1] ± 103
   Certificate <Cert> [0..1] Binary 104
3.4.4.2.10.2.1  Party <Pty>
Presence: [1..1]
Definition: Entity involved in an activity.
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
acmt.026.001.02 AccountListReportV02
Target2-Securities - Cash Account Query and Report 103 August 2026
```

