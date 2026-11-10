---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.31 Payment", "66.1.31.4 PaymentInstrument16", "66.1.31.4.3 AdditionalInformation <AddtlInf>"]
file_pages: [5058]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.31.4.3 AdditionalInformation <AddtlInf>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5058 to 5058.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5058

```text
66.1.31.4.3  AdditionalInformation <AddtlInf>
Presence: [0..*]
Definition: Additional information about the payment.
AdditionalInformation <AddtlInf> contains the following elements (see "AdditionalInformation15" on
page 4508 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InformationType <InfTp> [1..1] ± 4508
   InformationValue <InfVal> [1..1] Text 4508
66.1.32 Person Identification
66.1.32.1  IndividualPerson31
Definition: Human entity, as distinguished from a corporate entity (which is sometimes referred to as an
'artificial person').
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [0..1] Text 5058
   BirthDate <BirthDt> [0..1] Date 5059
   CountryAndResidentialStatus <CtryAndResdtlSts> [0..1] ± 5059
   BeneficiaryCertificationCompletion
<BnfcryCertfctnCmpltn>
[0..1] CodeSet 5059
   OtherIdentification <OthrId> [0..*]  5059
     Identification <Id> [1..1] Text 5060
     IdentificationType <IdTp> [1..1]  5060
{Or       Code <Cd> [1..1] CodeSet 5060
Or}       Proprietary <Prtry> [1..1] ± 5061
     Issuer <Issr> [0..1] Text 5061
Constraints
• PersonElementRule
One of the elements (Name, BirthDate, CountryAndResidentialStatus,
BeneficiaryCertificationCompletion, OtherIdentification) must be present.
66.1.32.1.1  Name <Nm>
Presence: [0..1]
Definition: Name by which the party is known and which is usually used to identify that party.
Datatype: "Max350Text" on page 5403
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5058 May 2026
```

