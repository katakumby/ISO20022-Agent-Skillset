---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CashAccountQueryAndReport"
source_ids: ["src-000351"]
source_editions: ["august-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.9 Person Identification"]
file_pages: [163]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.9 Person Identification

Source: [src-000351](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart2_Target2Securities_CashAccountQueryAndReport_v1.pdf`. Locator: one-based file pages 163 to 163.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 163

```text
ContactDetails <CtctDtls> contains the following elements (see "Contact13" on page 163 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   NamePrefix <NmPrfx> [0..1] CodeSet 164
   Name <Nm> [0..1] Text 164
   PhoneNumber <PhneNb> [0..1] Text 164
   MobileNumber <MobNb> [0..1] Text 165
   FaxNumber <FaxNb> [0..1] Text 165
   URLAddress <URLAdr> [0..1] Text 165
   EmailAddress <EmailAdr> [0..1] Text 165
   EmailPurpose <EmailPurp> [0..1] Text 165
   JobTitle <JobTitl> [0..1] Text 165
   Responsibility <Rspnsblty> [0..1] Text 165
   Department <Dept> [0..1] Text 165
   Other <Othr> [0..*]  166
     ChannelType <ChanlTp> [1..1] Text 166
     Identification <Id> [0..1] Text 166
   PreferredMethod <PrefrdMtd> [0..1] CodeSet 166
7.1.9 Person Identification
7.1.9.1  Contact13
Definition: Specifies the details of the contact person.
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
Message Items Types
Target2-Securities - Cash Account Query and Report 163 August 2026
```

