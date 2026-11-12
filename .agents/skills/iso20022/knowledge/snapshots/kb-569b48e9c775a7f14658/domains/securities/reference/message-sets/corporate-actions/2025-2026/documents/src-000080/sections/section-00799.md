---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.15 Miscellaneous", "16.1.15.68 BeneficiaryCertificationType13Choice"]
file_pages: [999]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.15.68 BeneficiaryCertificationType13Choice

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 999 to 999.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 999

```text
• Meaning When True: Yes
• Meaning When False: No
16.1.15.68  BeneficiaryCertificationType13Choice
Definition: Choice between a standard code or proprietary code to specify the type of beneficiary
certification required.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 999
Or}   Proprietary <Prtry> [1..1] ± 1000
16.1.15.68.1  Code <Cd>
Presence: [1..1]
Definition: Beneficial owner certification type expressed in a coded form.
Datatype: "BeneficiaryCertificationType6Code" on page 1164
CodeName Name Definition
ACCI AccreditedInvestor The holder of the security has to
irrevocably certify that it is an Accredited
Investor as defined in US Securities and
Exchange Commission Regulation D.
DOMI DomicileCountry The holder of the security has to certify
his domicile.
NDOM NonDomicileCountry The holder of the security has to certify,
in line with the terms of the corporate
action, that it is not domiciled in the
country indicated.
FULL FullBeneficialOwnerBreakdown The holder of the security has to provide
his beneficial owner details for
disclosure/instruction purpose.
NCOM NonCompany The holder of the security has to certify
he is an Non-Company related person.
QIBB QIBCertification The holder of the security has to
irrevocably certify that it is a Qualified
Institutional Buyer as defined in US
Securities and Exchange Commission
Rule 144A.
TRBD TaxRateBreakdown The holder of the security has to provide
basic details on nominals and associated
tax rate to be used by the account
servicer.
PABD ICSDParticipantBreakdown The (I)CSD has to provide its
participants' details for disclosure
purpose to the issuer/issuer's agent.
FRAC FractionBreakdown Indicates that the rounding rule in the
Fraction Disposition component at the
option level can be offered at the
beneficial owner level.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 999 February 2026
```

