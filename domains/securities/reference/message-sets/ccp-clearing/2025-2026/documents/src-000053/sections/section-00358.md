---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["12 Message Items Types", "12.1 MessageComponents", "12.1.14 Party Identification", "12.1.14.7 PartyIdentificationAndAccount31", "12.1.14.7.3 AdditionalInformation <AddtlInf>"]
file_pages: [451]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 12.1.14.7.3 AdditionalInformation <AddtlInf>

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 451 to 451.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 451

```text
AlternateIdentification <AltrnId> contains the following elements (see AlternatePartyIdentification4 on
page 445 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   IdentificationType <IdTp> [1..1] ± 445
   Country <Ctry> [1..1] CodeSet   'C5 445
   AlternateIdentification <AltrnId> [1..1] Text 446
12.1.14.7.3  AdditionalInformation <AddtlInf>
Presence: [0..1]
Definition: Provides additional information to a party identification.
Impacted by: C3 AdditonalDetailsGuideline
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
12.1.14.7.4  ClearingAccount <ClrAcct>
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
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
Message Items Types
March 2026 451
```

