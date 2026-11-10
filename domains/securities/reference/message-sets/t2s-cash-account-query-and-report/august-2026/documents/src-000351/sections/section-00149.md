---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CashAccountQueryAndReport"
source_ids: ["src-000351"]
source_editions: ["august-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.9 Person Identification", "7.1.9.1 Contact13", "7.1.9.1.1 NamePrefix <NmPrfx>"]
file_pages: [164]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.9.1.1 NamePrefix <NmPrfx>

Source: [src-000351](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart2_Target2Securities_CashAccountQueryAndReport_v1.pdf`. Locator: one-based file pages 164 to 164.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 164

```text
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
7.1.9.1.1  NamePrefix <NmPrfx>
Presence: [0..1]
Definition: Specifies the terms used to formally address a person.
Datatype: "NamePrefix2Code" on page 178
CodeName Name Definition
DOCT Doctor Title of the person is Doctor or Dr.
MADM Madam Title of the person is Madam.
MISS Miss Title of the person is Miss.
MIST Mister Title of the person is Mister or Mr.
MIKS GenderNeutral Title of the person is gender neutral
(Mx).
7.1.9.1.2  Name <Nm>
Presence: [0..1]
Definition: Name by which a party is known and which is usually used to identify that party.
Datatype: "Max140Text" on page 182
7.1.9.1.3  PhoneNumber <PhneNb>
Presence: [0..1]
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
Message Items Types
Target2-Securities - Cash Account Query and Report 164 August 2026
```

