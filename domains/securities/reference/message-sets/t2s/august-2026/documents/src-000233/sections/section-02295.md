---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.20 Party Identification", "82.1.20.9 PartyIdentification15"]
file_pages: [3076]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.20.9 PartyIdentification15

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 3076 to 3076.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3076

```text
ContactDetails <CtctDtls> contains the following elements (see "Contact13" on page 3084 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   NamePrefix <NmPrfx> [0..1] CodeSet 3084
   Name <Nm> [0..1] Text 3085
   PhoneNumber <PhneNb> [0..1] Text 3085
   MobileNumber <MobNb> [0..1] Text 3085
   FaxNumber <FaxNb> [0..1] Text 3085
   URLAddress <URLAdr> [0..1] Text 3085
   EmailAddress <EmailAdr> [0..1] Text 3085
   EmailPurpose <EmailPurp> [0..1] Text 3085
   JobTitle <JobTitl> [0..1] Text 3086
   Responsibility <Rspnsblty> [0..1] Text 3086
   Department <Dept> [0..1] Text 3086
   Other <Othr> [0..*]  3086
     ChannelType <ChanlTp> [1..1] Text 3086
     Identification <Id> [0..1] Text 3086
   PreferredMethod <PrefrdMtd> [0..1] CodeSet 3086
82.1.20.9  PartyIdentification15
Definition: Organised structure that is set up for a particular purpose, for example, a business,
government body, department, charity, or financial institution.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Country <Ctry> [0..1] CodeSet C3 3076
   Identification <Id> [1..1] Text 3077
82.1.20.9.1  Country <Ctry>
Presence: [0..1]
Definition: Country in which the organisation is registered.
Impacted by: C3 "Country"
Datatype: "CountryCode" on page 3234
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3076 August 2026
```

