---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S Billing"
source_ids: ["src-000346"]
source_editions: ["december-2025"]
message_ids: []
heading_path: ["3 camt.077.001.01 BillingReportV01", "3.4 Message Building Blocks"]
file_pages: [20]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.077.001.01"]
preceding_topic_continuations: [{"constraint_ids": ["C5", "C6"], "until_heading": "3.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 20, "topic": "3.3 Constraints", "reference_path": "domains/securities/reference/message-sets/t2s-billing/december-2025/documents/src-000346/sections/section-00012.md"}]
---

# 3.4 Message Building Blocks

Source: [src-000346](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart1_Target2Securities_Billing_v1.pdf`. Locator: one-based file pages 20 to 20.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

On file page 20, C5–C6 before **3.4 Message Building Blocks** continue [3.3 Constraints](section-00012.md). They belong to the preceding Constraints topic; the full source page is retained below without rearranging its text.
<!-- PDF-TOPIC-NAV-END -->

## File page 20

```text
C5 IBAN
A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.
C6 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
3.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
3.4.1 MessageHeader <MsgHdr>
Presence: [1..1]
Definition: Defines the characteristics specific to the message, such as the identification or the creation
date and time.
MessageHeader <MsgHdr> contains the following MessageHeader11 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 20
   CreationDateTime <CreDtTm> [0..1] DateTime 20
   RequestType <ReqTp> [0..1]  20
{Or     PaymentControl <PmtCtrl> [1..1] CodeSet 21
Or     Enquiry <Enqry> [1..1] CodeSet 21
Or}     Proprietary <Prtry> [1..1] ± 21
   OriginalBusinessQuery <OrgnlBizQry> [0..1] ± 21
3.4.1.1  MessageIdentification <MsgId>
Presence: [1..1]
Definition: Point to point reference, as assigned by the sender, to unambiguously identify the message.
Usage: The sender has to make sure that MessageIdentification is unique for a pre-agreed period.
Datatype: "Max35Text" on page 153
3.4.1.2  CreationDateTime <CreDtTm>
Presence: [0..1]
Definition: Date and time at which the message was created.
Datatype: "ISODateTime" on page 148
3.4.1.3  RequestType <ReqTp>
Presence: [0..1]
Approved by the Securities SEG on 20 November 2025 and the Payments
SEG on 01 December 2025, under the lead of the Securities Standards
Evaluation Group (SEG).
camt.077.001.01 BillingReportV01
Target2-Securities - Billing 20 December 2025
```

