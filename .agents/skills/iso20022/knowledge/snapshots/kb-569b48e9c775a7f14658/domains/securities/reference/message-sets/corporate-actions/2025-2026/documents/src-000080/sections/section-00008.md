---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "2.4 Message Building Blocks", "2.4.2 From <Fr>", "2.4.2.2 FinancialInstitutionIdentification <FIId>"]
file_pages: [13]
content_origin: "source-text-extraction"
mentioned_message_ids: ["head.001.001.02"]
---

# 2.4.2.2 FinancialInstitutionIdentification <FIId>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 13 to 13.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 13

```text
2.4.2.2  FinancialInstitutionIdentification <FIId>
Presence: [1..1]
Definition: Identification of a financial institution.
FinancialInstitutionIdentification <FIId> contains the following elements (see
"BranchAndFinancialInstitutionIdentification6" on page 867 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstitutionIdentification <FinInstnId> [1..1] ± 867
   BranchIdentification <BrnchId> [0..1] ± 868
2.4.3 To <To>
Presence: [1..1]
Definition: The MessagingEndpoint designated by the sending MessagingEndpoint to be the recipient
who will ultimately process this Business Message.
Note the receiving MessagingEndpoint might be different from the receiving address potentially
contained in the transport header (as defined in the transport layer).
To <To> contains one of the following Party44Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   OrganisationIdentification <OrgId> [1..1] ± 13
Or}   FinancialInstitutionIdentification <FIId> [1..1] ± 13
2.4.3.1  OrganisationIdentification <OrgId>
Presence: [1..1]
Definition: Identification of a person or an organisation.
OrganisationIdentification <OrgId> contains the following elements (see "PartyIdentification135" on
page 1040 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [0..1] Text 1040
   PostalAddress <PstlAdr> [0..1] ± 1040
   Identification <Id> [0..1] ± 1041
   CountryOfResidence <CtryOfRes> [0..1] CodeSet C3 1041
   ContactDetails <CtctDtls> [0..1] ± 1042
2.4.3.2  FinancialInstitutionIdentification <FIId>
Presence: [1..1]
Definition: Identification of a financial institution.
Approved by the Securities SEG on 27 January 2026 head.001.001.02 BusinessApplicationHeaderV02
Corporate Actions - Maintenance 2025 - 2026 13 February 2026
```

