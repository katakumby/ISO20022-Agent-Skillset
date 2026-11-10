---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.15 Miscellaneous", "16.1.15.71 CorporateActionEventType107Choice", "16.1.15.71.2 Proprietary <Prtry>"]
file_pages: [1021]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.15.71.2 Proprietary <Prtry>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 1021 to 1021.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1021

```text
CodeName Name Definition
TNDP TaxOnNonDistributedProceeds Taxable component on non-distributed
proceeds, for example, Australian
deemed income or US 871m income
regulation.
RCLA Reclassification Securities related event which
reclassifies the distribution in various
types of income for US tax withholding
purposes.
16.1.15.71.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Event type expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 879 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 879
   Issuer <Issr> [1..1] Text 879
   SchemeName <SchmeNm> [0..1] Text 880
16.1.15.72  AdditionalBusinessProcessFormat23Choice
Definition: Choice between a standard code or proprietary code to specify the type of the additional
business process, that is, a tax refund.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1021
Or}   Proprietary <Prtry> [1..1] ± 1022
16.1.15.72.1  Code <Cd>
Presence: [1..1]
Definition: Standard code to specify the additional business process "tax refund" linked to a corporate
action event.
Datatype: "AdditionalBusinessProcess12Code" on page 1159
CodeName Name Definition
CLFT FullTransferOfReceivedProceeds Market Claim is to transfer proceeds
received from the issuer to the entitled
party.
CLAI ClaimOrCompensation Relates to a claim on the associated
corporate action event.
CLNT PartialTransferOfReceivedProceeds Market Claim is to transfer proceeds
partially received from the issuer to the
entitled party. Part is compensated in
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1021 February 2026
```

