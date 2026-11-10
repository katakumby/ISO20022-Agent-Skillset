---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "Business Application Header"
source_ids: ["src-000011"]
source_editions: ["Version 4 March 2024"]
message_ids: []
heading_path: ["2 head.001.001.04 BusinessApplicationHeaderV04", "2.4 Message Building Blocks"]
file_pages: [9]
content_origin: "source-text-extraction"
mentioned_message_ids: ["head.001.001.04"]
---

# 2.4 Message Building Blocks

Source: [src-000011](../../../../../../../../raw-input/business_application_header/ISO20022_MDR_bahV4_v1.pdf). Locator: one-based file pages 9 to 9.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 9

```text
C6 ValidationByTable
C7 ValidationByTable
2.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
2.4.1 CharacterSet <CharSet>
Presence: [0..1]
Definition: Contains the character set of the text-based elements used in the Business Message.
Impacted by: C6 "ValidationByTable"
Datatype: "UnicodeChartsCode" on page 53
Constraints
• ValidationByTable
2.4.2 From <Fr>
Presence: [1..1]
Definition: The sending MessagingEndpoint that has created this Business Message for the receiving
MessagingEndpoint that will process this Business Message.
Note the sending MessagingEndpoint might be different from the sending address potentially contained
in the transport header (as defined in the transport layer).
From <Fr> contains one of the following Party51Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   OrganisationIdentification <OrgId> [1..1] ± 9
Or}   FinancialInstitutionIdentification <FIId> [1..1] ± 10
2.4.2.1  OrganisationIdentification <OrgId>
Presence: [1..1]
Definition: Identification of a person or an organisation.
Approved by the Cross-SEG Harmonisation SEG on 20 February 2024 head.001.001.04 BusinessApplicationHeaderV04
Business Application Header - Version 4 9 March 2024
```

