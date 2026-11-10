---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S LimitUtilisationJournal"
source_ids: ["src-000363"]
source_editions: ["february-2025"]
message_ids: []
heading_path: ["3 camt.065.001.01 LimitUtilisationJournalReportV01", "3.4 Message Building Blocks"]
file_pages: [12]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.065.001.01"]
---

# 3.4 Message Building Blocks

Source: [src-000363](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LimitUtilisationJournal_MessageSet/ISO20022_MDRPart2_Target2Securities_LimitUtilisationJournal_v1.pdf`. Locator: one-based file pages 12 to 12.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 12

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
Presence: [0..1]
Definition: Set of elements used to provide information on the header of the message.
MessageHeader <MsgHdr> contains the following MessageHeader12 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 12
   CreationDateTime <CreDtTm> [0..1] DateTime 12
   OriginalBusinessInstruction <OrgnlBizInstr> [0..1] ± 12
3.4.1.1  MessageIdentification <MsgId>
Presence: [1..1]
Definition: Point to point reference, as assigned by the sender, to unambiguously identify the message.
Usage: The sender has to make sure that MessageIdentification is unique for a pre-agreed period.
Datatype: "Max35Text" on page 46
3.4.1.2  CreationDateTime <CreDtTm>
Presence: [0..1]
Definition: Date and time at which the message was created.
Datatype: "ISODateTime" on page 43
3.4.1.3  OriginalBusinessInstruction <OrgnlBizInstr>
Presence: [0..1]
Definition: Unique identification of the original instruction.
Approved by the Securities on the 16th January 2025 and Payments SEG on
the 24th January 2025 under the lead of the Securities SEG.
camt.065.001.01 LimitUtilisationJournalReportV01
Target2-Securities - Limit Utilisation Journal 12 February 2025
```

