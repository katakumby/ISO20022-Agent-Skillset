---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Party Identification", "7.1.19.9 PartyIdentification15"]
file_pages: [430]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.9 PartyIdentification15

Source: [src-000375](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 430 to 430.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 430

```text
ContactDetails <CtctDtls> contains the following elements (see "Contact13" on page 434 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   NamePrefix <NmPrfx> [0..1] CodeSet 435
   Name <Nm> [0..1] Text 435
   PhoneNumber <PhneNb> [0..1] Text 435
   MobileNumber <MobNb> [0..1] Text 436
   FaxNumber <FaxNb> [0..1] Text 436
   URLAddress <URLAdr> [0..1] Text 436
   EmailAddress <EmailAdr> [0..1] Text 436
   EmailPurpose <EmailPurp> [0..1] Text 436
   JobTitle <JobTitl> [0..1] Text 436
   Responsibility <Rspnsblty> [0..1] Text 436
   Department <Dept> [0..1] Text 436
   Other <Othr> [0..*]  437
     ChannelType <ChanlTp> [1..1] Text 437
     Identification <Id> [0..1] Text 437
   PreferredMethod <PrefrdMtd> [0..1] CodeSet 437
7.1.19.9  PartyIdentification15
Definition: Organised structure that is set up for a particular purpose, for example, a business,
government body, department, charity, or financial institution.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Country <Ctry> [0..1] CodeSet C3 430
   Identification <Id> [1..1] Text 431
7.1.19.9.1  Country <Ctry>
Presence: [0..1]
Definition: Country in which the organisation is registered.
Impacted by: C3 "Country"
Datatype: "CountryCode" on page 501
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 430 March 2026
```

