---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.13 Payment"]
file_pages: [563]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.13 Payment

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 563 to 563.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 563

```text
ContactDetails <CtctDtls> contains the following elements (see "Contact13" on page 572 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   NamePrefix <NmPrfx> [0..1] CodeSet 572
   Name <Nm> [0..1] Text 573
   PhoneNumber <PhneNb> [0..1] Text 573
   MobileNumber <MobNb> [0..1] Text 573
   FaxNumber <FaxNb> [0..1] Text 573
   URLAddress <URLAdr> [0..1] Text 573
   EmailAddress <EmailAdr> [0..1] Text 573
   EmailPurpose <EmailPurp> [0..1] Text 573
   JobTitle <JobTitl> [0..1] Text 573
   Responsibility <Rspnsblty> [0..1] Text 574
   Department <Dept> [0..1] Text 574
   Other <Othr> [0..*]  574
     ChannelType <ChanlTp> [1..1] Text 574
     Identification <Id> [0..1] Text 574
   PreferredMethod <PrefrdMtd> [0..1] CodeSet 574
6.1.13 Payment
6.1.13.1  InstructionForCreditorAgent3
Definition: Further information related to the processing of the payment instruction that may need to be
acted upon by the creditor's agent. The instruction may relate to a level of service, or may be an
instruction that has to be executed by the creditor's agent, or may be information required by the
creditor's agent.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [0..1] CodeSet 563
   InstructionInformation <InstrInf> [0..1] Text 564
6.1.13.1.1  Code <Cd>
Presence: [0..1]
Definition: Coded information related to the processing of the payment instruction, provided by the
initiating party, and intended for the creditor's agent.
Datatype: "ExternalCreditorAgentInstruction1Code" on page 592
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Initiation - Maintenance 2025 - 2026 563 March 2026
```

