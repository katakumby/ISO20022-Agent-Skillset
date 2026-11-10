---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.26 Status", "16.1.26.11 PendingReason70Choice", "16.1.26.11.2 Proprietary <Prtry>"]
file_pages: [1154]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.26.11.2 Proprietary <Prtry>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 1154 to 1154.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1154

```text
CodeName Name Definition
NPAY NoPayment Payment has not been made by issuer.
NSEC NotDelivered Financial instruments have not been
delivered by the issuer.
OTHR Other Other. See Narrative.
AUTH SentToTaxAuthorities Instruction/event is pending because the
reclaim is sent to the tax authorities.
16.1.26.11.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Proprietary identification of the reason why the instruction/event has a pending status.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 879 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 879
   Issuer <Issr> [1..1] Text 879
   SchemeName <SchmeNm> [0..1] Text 880
16.1.26.12  AcceptedStatus2
Definition: Status and quantity information related to an accepted instruction request.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AcceptedQuantity <AccptdQty> [0..1] ± 1154
   AcceptedReason <AccptdRsn> [1..1] ± 1154
16.1.26.12.1  AcceptedQuantity <AccptdQty>
Presence: [0..1]
Definition: Quantity of instructed securities that has been accepted for further processing.
AcceptedQuantity <AccptdQty> contains one of the following elements (see "Quantity51Choice" on
page 1090 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Quantity <Qty> [1..1] ± C13 1091
Or}   OriginalAndCurrentFace <OrgnlAndCurFace> [1..1] ± 1091
16.1.26.12.2  AcceptedReason <AccptdRsn>
Presence: [1..1]
Definition: Reason for the accepted status.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1154 February 2026
```

