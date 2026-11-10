---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["12 Message Items Types", "12.1 MessageComponents", "12.1.14 Party Identification", "12.1.14.12 PartyIdentificationAndAccount227", "12.1.14.12.4 ClearingAccount <ClrAcct>"]
file_pages: [458]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 12.1.14.12.4 ClearingAccount <ClrAcct>

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 458 to 458.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 458

```text
AdditionalInformation <AddtlInf> contains the following elements (see PartyTextInformation1 on
page 449 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DeclarationDetails <DclrtnDtls> [0..1] Text 449
   PartyContactDetails <PtyCtctDtls> [0..1] Text 449
   RegistrationDetails <RegnDtls> [0..1] Text 450
Constraints
• AdditonalDetailsGuideline
(Guideline)
Unless bilaterally agreed between the Sender and Receiver, DeclarationlDetails, RegistrationDetails
and PartyContactDetails must not contain information that can be provided in a structured field.
12.1.14.12.4  ClearingAccount <ClrAcct>
Presence: [0..1]
Definition: Identifies the clearing member account at the Central counterparty through which the trade
must be cleared (sometimes called position account).
ClearingAccount <ClrAcct> contains the following elements (see SecuritiesAccount18 on page 373
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 373
   Type <Tp> [1..1] CodeSet 373
   Name <Nm> [0..1] Text 373
12.1.15 Person Identification
12.1.15.1  ContactIdentification2
Definition: Information needed to contact a physical person.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   NamePrefix <NmPrfx> [0..1] CodeSet 459
   GivenName <GvnNm> [0..1] Text 459
   Name <Nm> [1..1] Text 459
   PhoneNumber <PhneNb> [0..1] Text 459
   MobileNumber <MobNb> [0..1] Text 459
   FaxNumber <FaxNb> [0..1] Text 459
   EmailAddress <EmailAdr> [0..1] Text 459
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
Message Items Types
March 2026 458
```

